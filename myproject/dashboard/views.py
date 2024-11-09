from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from dashboard.Angel.utils import get_position, login_to_angel, buy, get_token, sell, BuyLmt, SellLmt, get_ltp
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import calendar


@require_GET
def fetch_symbol_data(request):
    symbol = request.GET.get('symbol')
    print(f"Selected symbol: {symbol}")

    LTP = 0
    rounded_LTP = 0
    strikes = []

    # Determine LTP and strike differences based on the symbol
    if symbol == "NIFTY":
        LTP = get_ltp(segment="NSE", symbol="Nifty 50", token=get_token("Nifty 50"))
        rounded_LTP = round(LTP / 50) * 50  # Round to nearest 50
        strike_difference = 50
    elif symbol == "BANKNIFTY":
        LTP = get_ltp(segment="NSE", symbol="Nifty Bank", token=get_token("Nifty Bank"))
        rounded_LTP = round(LTP / 100) * 100  # Round to nearest 100
        strike_difference = 100
    elif symbol == "MIDCAPNIFTY":
        LTP = get_ltp(segment="NSE", symbol="MIDCAP-EQ", token=get_token("MIDCAP-EQ"))
        rounded_LTP = round(LTP / 25) * 25  # Round to nearest 25
        strike_difference = 25
    elif symbol == "FINNIFTY":
        LTP = get_ltp(segment="NSE", symbol="Nifty 50", token=get_token("Nifty 50"))
        rounded_LTP = round(LTP / 50) * 50  # Round to nearest 50
        strike_difference = 50
    else:
        # Handle unsupported symbols
        return JsonResponse({"error": "Unsupported symbol"}, status=400)

    print(f"Rounded LTP: {rounded_LTP}")

    # Generate 10 strikes up and down from the rounded LTP
    strikes = [rounded_LTP + i * strike_difference for i in range(-10, 11)]

    # Ensure strikes are sorted
    strikes.sort()

    # Prepare the response with sorted strikes and rounded_LTP as default
    response_data = {
        'symbol': symbol,
        'LTP': round(LTP, 2),
        'rounded_LTP': rounded_LTP,
        'strikes': strikes
    }

    print(response_data)
    return JsonResponse(response_data)


def dashboard_view(request):
    return render(request, 'dashboard.html')


def api_login(request):
    if request.method == 'POST':
        try:
            login_to_angel()
            get_position()
            return redirect('dashboard')  # Redirect to the dashboard after successful login
        except Exception as e:
            print(e)
            return render(request, 'dashboard.html', {'error': str(e)})
    return render(request, 'dashboard.html')


def futidx_buy(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        expiry = request.POST.get('expiry')
        quantity = request.POST.get('quantity')
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
        # Print the values to the console for debugging purposes
        print(f"Symbol: {symbol}")
        print(f"Expiry: {expiry}")
        print(f"Quantity: {quantity}")
        day = expiry_date.strftime("%d")
        month = expiry_date.strftime("%b").upper()
        year = expiry_date.strftime("%y")
        formatted_symbol = f"{symbol}{day}{month}{year}FUT"
        print(f"Buy order executed @ : {formatted_symbol}")

        buy(symbol=formatted_symbol, token=get_token(formatted_symbol), quantity=quantity, exchange='NFO')

    return render(request, 'dashboard.html')


def futidx_sell(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        expiry = request.POST.get('expiry')
        quantity = request.POST.get('quantity')
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
        day = expiry_date.strftime("%d")
        month = expiry_date.strftime("%b").upper()
        year = expiry_date.strftime("%y")
        formatted_symbol = f"{symbol}{day}{month}{year}FUT"
        print(f"Sell order executed @ : {formatted_symbol}")
        # Sell operation
        sell(symbol=formatted_symbol, token=get_token(formatted_symbol), quantity=quantity, exchange='NFO')

    return render(request, 'dashboard.html')


def b_action(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        expiry = request.POST.get('expiry')
        quantity = request.POST.get('limit_qty')  # Use limit quantity for B
        limit_price = request.POST.get('limit_price')  # Use limit price for B
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
        day = expiry_date.strftime("%d")
        month = expiry_date.strftime("%b").upper()
        year = expiry_date.strftime("%y")
        formatted_symbol = f"{symbol}{day}{month}{year}FUT"
        # Perform Buy Action (B)
        print(
            f"Buy Action - Symbol: {formatted_symbol}, Quantity: {quantity}, Limit Price: {limit_price}, Limit Qty: {quantity}")
        BuyLmt(symbol=formatted_symbol, token=get_token(formatted_symbol), quantity=quantity, exchange='NFO',
               price=limit_price)

    return render(request, 'dashboard.html')


def s_action(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        expiry = request.POST.get('expiry')
        quantity = request.POST.get('quantity')
        limit_price = request.POST.get('sell-limit-price')
        limit_qty = request.POST.get('sell-limit-qty')

        expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
        day = expiry_date.strftime("%d")
        month = expiry_date.strftime("%b").upper()
        year = expiry_date.strftime("%y")
        formatted_symbol = f"{symbol}{day}{month}{year}FUT"

        # Perform Sell Action (S)
        print(
            f"Sell Action - Symbol: {formatted_symbol}, Quantity: {quantity}, Limit Price: {limit_price}, Limit Qty: {limit_qty}")
        SellLmt(symbol=formatted_symbol, token=get_token(formatted_symbol), quantity=quantity, exchange='NFO',
                price=limit_price)

    return render(request, 'dashboard.html')


# market order buy optidx ce
def buy_ce_optidx(request):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        expiry = request.POST.get('expiry')
        symbol = request.POST.get('symbol')
        strike = request.POST.get('strike')
        print(f"BUY CE -> Quantity: {quantity}, Expiry: {expiry}, Symbol: {symbol}, Strike: {strike}")
        # Implement actual buy CE logic here
        #     NIFTY07NOV2423500CE (WEEKLY)
        #     NIFTY28NOV2424200CE
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
        day = expiry_date.strftime("%d")
        month = expiry_date.strftime("%b").upper()
        year = expiry_date.strftime("%y")
        formatted_symbol = f"{symbol}{day}{month}{year}{strike}CE"
        buy(symbol=formatted_symbol, token=get_token(formatted_symbol), quantity=quantity, exchange='NFO')

    return render(request, 'dashboard.html')


# market order sell optidx ce
def sell_ce_optidx(request):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        expiry = request.POST.get('expiry')
        symbol = request.POST.get('symbol')
        strike = request.POST.get('strike')
        print(f"Sell CE -> Quantity: {quantity}, Expiry: {expiry}, Symbol: {symbol}, Strike: {strike}")
        # Implement actual buy CE logic here
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
        day = expiry_date.strftime("%d")
        month = expiry_date.strftime("%b").upper()
        year = expiry_date.strftime("%y")
        formatted_symbol = f"{symbol}{day}{month}{year}{strike}CE"
        sell(symbol=formatted_symbol, token=get_token(formatted_symbol), quantity=quantity, exchange='NFO')

    return render(request, 'dashboard.html')


# market order buy optidx pe
def buy_pe_optidx(request):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        expiry = request.POST.get('expiry')
        symbol = request.POST.get('symbol')
        strike = request.POST.get('strike')
        print(f"BUY PE -> Quantity: {quantity}, Expiry: {expiry}, Symbol: {symbol}, Strike: {strike}")
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
        day = expiry_date.strftime("%d")
        month = expiry_date.strftime("%b").upper()
        year = expiry_date.strftime("%y")
        formatted_symbol = f"{symbol}{day}{month}{year}{strike}PE"
        buy(symbol=formatted_symbol, token=get_token(formatted_symbol), quantity=quantity, exchange='NFO')

    return render(request, 'dashboard.html')


# market order sell optidx ce
def sell_pe_optidx(request):
    quantity = request.POST.get('quantity')
    expiry = request.POST.get('expiry')
    symbol = request.POST.get('symbol')
    strike = request.POST.get('strike')
    print(f"Sell PE -> Quantity: {quantity}, Expiry: {expiry}, Symbol: {symbol}, Strike: {strike}")
    expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
    day = expiry_date.strftime("%d")
    month = expiry_date.strftime("%b").upper()
    year = expiry_date.strftime("%y")
    formatted_symbol = f"{symbol}{day}{month}{year}{strike}PE"
    buy(symbol=formatted_symbol, token=get_token(formatted_symbol), quantity=quantity, exchange='NFO')

    return render(request, 'dashboard.html')


#  limit order view in optidx

# limit order buy optidx ce
def buy_call_optidx(request):
    if request.method == 'POST':
        strike = request.POST.get('strike')
        limit_price = request.POST.get('limitPrice')
        limit_qty = request.POST.get('limitQty')
        symbol = request.POST.get('symbol')
        expiry = request.POST.get('expiry')
        print(f"Buy Call - Strike: {strike}, Limit Price: {limit_price}, Limit Qty: {limit_qty},{symbol}")
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
        day = expiry_date.strftime("%d")
        month = expiry_date.strftime("%b").upper()
        year = expiry_date.strftime("%y")
        formatted_symbol = f"{symbol}{day}{month}{year}{strike}CE"
        # Implement order logic here
        BuyLmt(symbol=formatted_symbol, token=get_token(formatted_symbol), quantity=limit_qty, exchange='NFO',
               price=limit_price)

    return render(request, 'dashboard.html')


# limit order sell optidx ce
# View for Sell in Call section
def sell_call_optidx(request):
    if request.method == 'POST':
        strike = request.POST.get('strike')
        limit_price = request.POST.get('limitPrice')
        limit_qty = request.POST.get('limitQty')
        symbol = request.POST.get('symbol')
        expiry = request.POST.get('expiry')
        print(f"Buy Call - Strike: {strike}, Limit Price: {limit_price}, Limit Qty: {limit_qty},{symbol}")
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
        day = expiry_date.strftime("%d")
        month = expiry_date.strftime("%b").upper()
        year = expiry_date.strftime("%y")
        formatted_symbol = f"{symbol}{day}{month}{year}{strike}CE"
        # Implement order logic here
        SellLmt(symbol=formatted_symbol, token=get_token(formatted_symbol), quantity=limit_qty, exchange='NFO',
                price=limit_price)

    return render(request, 'dashboard.html')


# limit order buy optidx pe
# View for Buy in Put section
def buy_put_optidx(request):
    if request.method == 'POST':
        strike = request.POST.get('strike')
        limit_price = request.POST.get('limitPrice')
        limit_qty = request.POST.get('limitQty')
        symbol = request.POST.get('symbol')
        expiry = request.POST.get('expiry')
        print(f"Buy Put - Strike: {strike}, Limit Price: {limit_price}, Limit Qty: {limit_qty},{symbol}")
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
        day = expiry_date.strftime("%d")
        month = expiry_date.strftime("%b").upper()
        year = expiry_date.strftime("%y")
        formatted_symbol = f"{symbol}{day}{month}{year}{strike}PE"
        # Implement order logic here
        BuyLmt(symbol=formatted_symbol, token=get_token(formatted_symbol), quantity=limit_qty, exchange='NFO',
               price=limit_price)

    return render(request, 'dashboard.html')


# limit order sell optidx pe
# View for Sell in Put section
def sell_put_optidx(request):
    if request.method == 'POST':
        strike = request.POST.get('strike')
        limit_price = request.POST.get('limitPrice')
        limit_qty = request.POST.get('limitQty')
        symbol = request.POST.get('symbol')
        expiry = request.POST.get('expiry')
        print(f"Buy Put - Strike: {strike}, Limit Price: {limit_price}, Limit Qty: {limit_qty},{symbol}")
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
        day = expiry_date.strftime("%d")
        month = expiry_date.strftime("%b").upper()
        year = expiry_date.strftime("%y")
        formatted_symbol = f"{symbol}{day}{month}{year}{strike}PE"
        # Implement order logic here
        SellLmt(symbol=formatted_symbol, token=get_token(formatted_symbol), quantity=limit_qty, exchange='NFO',
                price=limit_price)

    return render(request, 'dashboard.html')


# net pos view
def fetch_positions(request):
    # Sample response mimicking the broker's data
    net_positions_response = get_position()

    if net_positions_response['status']:
        return JsonResponse(net_positions_response['data'], safe=False)
    else:
        return JsonResponse([], safe=False)


#  ltp fetch spot optidx pannel
def fetch_ltp_only(request):
    symbol = request.GET.get('symbol')
    LTP = 0

    if symbol == "NIFTY":
        LTP = get_ltp(segment="NSE", symbol="Nifty 50", token=get_token("Nifty 50"))
    elif symbol == "BANKNIFTY":
        LTP = get_ltp(segment="NSE", symbol="Nifty Bank", token=get_token("Nifty Bank"))
    elif symbol == "MIDCAPNIFTY":
        LTP = get_ltp(segment="NSE", symbol="MIDCAP-EQ", token=get_token("MIDCAP-EQ"))
    elif symbol == "FINNIFTY":
        LTP = get_ltp(segment="NSE", symbol="Nifty 50", token=get_token("Nifty 50"))
    else:
        return JsonResponse({"error": "Unsupported symbol"}, status=400)

    return JsonResponse({"symbol": symbol, "LTP": round(LTP, 2)})


#  update call and put ltp
def get_last_thursday(year, month):
    """Returns the date of the last Thursday of a given month."""
    last_day = calendar.monthrange(year, month)[1]  # Last day of the month
    last_date = datetime(year, month, last_day)
    while last_date.weekday() != calendar.THURSDAY:
        last_date -= timedelta(days=1)
    return last_date.date()


def update_call_put_ltp(request):
    symbol = request.GET.get('symbol')
    expiry_str = request.GET.get('expiry')  # Expected in YYYY-MM-DD format
    call_strike = request.GET.get('call_strike')
    put_strike = request.GET.get('put_strike')

    try:
        # Convert expiry date format to DDMMMYY (e.g., 14NOV24)
        expiry_date = datetime.strptime(expiry_str, '%Y-%m-%d').date()
        converted_expiry = expiry_date.strftime('%d%b%y').upper()
    except ValueError:
        return JsonResponse({'error': 'Invalid expiry date format'}, status=400)

    # Construct symbols for Call and Put
    callsym = f"{symbol}{converted_expiry}{call_strike}CE"
    putsym = f"{symbol}{converted_expiry}{put_strike}PE"

    # Assuming `get_ltp` and `get_token` are functions defined elsewhere
    call_ltp = get_ltp(segment="NFO", symbol=callsym, token=get_token(callsym))
    put_ltp = get_ltp(segment="NFO", symbol=putsym, token=get_token(putsym))
    print(f"{callsym}: ", call_ltp)

    response_data = {
        'call_symbol': callsym,
        'put_symbol': putsym,
        'call_ltp': call_ltp,
        'put_ltp': put_ltp,
        'symbol': symbol,
        'expiry_date': expiry_str
    }
    return JsonResponse(response_data)

# def update_call_put_ltp(request):
#     # Extract the expiry date from the request
#     symbol = request.GET.get('symbol')
#     expiry_str = request.GET.get('expiry')  # Expected in YYYY-MM-DD format
#     expiry_date = datetime.strptime(expiry_str, '%Y-%m-%d').date()
#     converted_expiry = expiry_date.strftime('%d%b%y').upper()
#     call_strike = request.GET.get('call_strike')
#     put_strike = request.GET.get('put_strike')
#     callsym = f"{symbol}{converted_expiry}{call_strike}CE"
#     putsym = f"{symbol}{converted_expiry}{put_strike}PE"
#     call_ltp = get_ltp(segment="NFO", symbol=callsym, token=get_token(callsym))
#     put_ltp = get_ltp(segment="NFO", symbol=putsym, token=get_token(putsym))
#     print("call_ltp: ", call_ltp)
#     print("put_ltp: ", put_ltp)
#
#     response_data = {
#
#         'call_ltp': call_ltp,
#         'put_ltp': put_ltp,
#         'symbol': symbol,
#         'expiry_date': expiry_str
#     }
#     return JsonResponse(response_data)

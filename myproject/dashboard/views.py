from datetime import datetime
from django.shortcuts import render, redirect
from dashboard.Angel.utils import login_to_angel,buy,get_token,sell,BuyLmt,SellLmt,get_ltp
from django.http import JsonResponse
from django.views.decorators.http import require_GET


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
            login_to_angel()  # Call the login function from utils.py
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


    return render(request,'dashboard.html')


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
        print(f"Buy Action - Symbol: {formatted_symbol}, Quantity: {quantity}, Limit Price: {limit_price}, Limit Qty: {quantity}")
        BuyLmt(symbol=formatted_symbol, token=get_token(formatted_symbol), quantity=quantity, exchange='NFO',price=limit_price)


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
        print(f"Sell Action - Symbol: {formatted_symbol}, Quantity: {quantity}, Limit Price: {limit_price}, Limit Qty: {limit_qty}")
        SellLmt(symbol=formatted_symbol, token=get_token(formatted_symbol), quantity=quantity, exchange='NFO',price=limit_price)

    return render(request, 'dashboard.html')

import datetime
from SmartApi.smartExceptions import DataException
import pandas as pd
import requests
from .SmartApi import SmartConnect  # Importing SmartConnect directly
import pyotp
from logzero import logger
import pandas_ta as ta
import os


apikey="Sg2W3HFf"
secret="9e400a02-cf6a-4e03-887e-a436f413cd36"
USERNAME="S60612177"
PASSWORD="Akki123@"
totp_string="D45IFKPPHUFT3OHK7OAWMSLUCA"
pin = "1234"
smartApi=None


def login(api_key, username, pwd, totp_string):
    global smartApi
    print("print inside angel integration")
    api_key = api_key
    username = username
    pwd = pwd
    print(username)
    print(pwd)
    smartApi = SmartConnect(api_key=api_key)
    print("smartApi: ", smartApi)
    try:
        token = totp_string
        totp = pyotp.TOTP(token).now()
    except Exception as e:
        logger.error("Invalid Token: The provided token is not valid.")
        raise e
    correlation_id = "abcde"
    data = smartApi.generateSession(username, pwd, totp)
    if data['status'] == False:
        logger.error(data)
    else:
        authToken = data['data']['jwtToken']
        refreshToken = data['data']['refreshToken']
        feedToken = smartApi.getfeedToken()
        res = smartApi.getProfile(refreshToken)
        smartApi.generateToken(refreshToken)
        res = res['data']['exchanges']
        print(smartApi.getProfile(refreshToken))

    return smartApi  # Return the smartApi instance if needed


def get_ltp(segment,symbol,token):
    global smartApi
    res=smartApi.ltpData(segment,symbol,token)
    ltp_value = res['data']['ltp']
    return ltp_value


def symbolmpping():
    url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
    d = requests.get(url).json()
    tokendf = pd.DataFrame.from_dict(d)
    tokendf['expiry'] = pd.to_datetime(tokendf['expiry'])
    tokendf = tokendf.astype({'strike': float})
    instrument_path = os.path.join(os.path.dirname(__file__), 'Instrument.csv')
    print("Instrument file generation")
    tokendf.to_csv(instrument_path, index=False)  # Save the CSV file in the Angel folder


def get_historical_data(symbol, token, timeframe, segment):
    global smartApi
    try:
        historicParam = {
            "exchange": segment,
            "symboltoken": token,
            "interval": timeframe,
            "fromdate": "2024-02-08 09:00",
            "todate": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        }
        res = smartApi.getCandleData(historicParam)
        df = pd.DataFrame(res['data'], columns=['date', 'open', 'high', 'low', 'close', 'flag'])
        pf = ta.ha(df['open'], df['high'], df['low'], df['close'])


        for column in pf.columns:
            df[column] = pf[column]

        df['date'] = pd.to_datetime(df['date'])
        df.to_csv(f"{symbol}.csv")
        return df

    except Exception as e:
        logger.exception(f"Historic Api failed: {e}")

def buy(symbol,token,quantity,exchange):
    global smartApi
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": symbol,
            "symboltoken": token,
            "transactiontype": "BUY",
            "exchange": exchange,
            "ordertype": "MARKET",
            "producttype": "INTRADAY",
            "duration": "DAY",
            "price": "0",
            "squareoff": "0",
            "stoploss": "0",
            "quantity": quantity
        }
        # Method 1: Place an order and return the order ID
        orderid = smartApi.placeOrder(orderparams)
        logger.info(f"PlaceOrder : {orderid}")
        print(orderid)
    except Exception as e:
        logger.exception(f"Order placement failed: {e}")
        print(e)
    except SmartApi.smartExceptions.DataException as e:
        print("error",e)
        logger.error(f"Order placement failed: {e}")
        print(e)

def BuyLmt(symbol,token,quantity,exchange,price):
    global smartApi
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": symbol,
            "symboltoken": token,
            "transactiontype": "BUY",
            "exchange": exchange,
            "ordertype": "LIMIT",
            "producttype": "INTRADAY",
            "duration": "DAY",
            "price": price,
            "squareoff": "0",
            "stoploss": "0",
            "quantity": quantity
        }
        # Method 1: Place an order and return the order ID
        orderid = smartApi.placeOrder(orderparams)
        logger.info(f"PlaceOrder : {orderid}")
        print(orderid)
    except Exception as e:
        logger.exception(f"Order placement failed: {e}")
        print(e)
    except SmartApi.smartExceptions.DataException as e:
        print("error",e)
        logger.error(f"Order placement failed: {e}")
        print(e)

def SellLmt(symbol,token,quantity,exchange,price):
    global smartApi
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": symbol,
            "symboltoken": token,
            "transactiontype": "SELL",
            "exchange": exchange,
            "ordertype": "LIMIT",
            "producttype": "INTRADAY",
            "duration": "DAY",
            "price": price,
            "squareoff": "0",
            "stoploss": "0",
            "quantity": quantity
        }
        # Method 1: Place an order and return the order ID
        orderid = smartApi.placeOrder(orderparams)
        logger.info(f"PlaceOrder : {orderid}")
        print(orderid)
    except Exception as e:
        logger.exception(f"Order placement failed: {e}")
        print(e)
    except SmartApi.smartExceptions.DataException as e:
        print("error", e)
        logger.error(f"Order placement failed: {e}")
        print(e)


def sell(symbol,token,quantity,exchange):
    global smartApi
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": symbol,
            "symboltoken": token,
            "transactiontype": "SELL",
            "exchange": exchange,
            "ordertype": "MARKET",
            "producttype": "INTRADAY",
            "duration": "DAY",
            "price": "0",
            "squareoff": "0",
            "stoploss": "0",
            "quantity": quantity
        }
        # Method 1: Place an order and return the order ID
        orderid = smartApi.placeOrder(orderparams)
        logger.info(f"PlaceOrder : {orderid}")
        print(orderid)
    except Exception as e:
        logger.exception(f"Order placement failed: {e}")
        print(e)
    except SmartApi.smartExceptions.DataException as e:
        print("error", e)
        logger.error(f"Order placement failed: {e}")
        print(e)


def SHORT(symbol,token,quantity,exchange):
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": symbol,
            "symboltoken": token,
            "transactiontype": "SELL",
            "exchange": exchange,
            "ordertype": "MARKET",
            "producttype": "INTRADAY",
            "duration": "DAY",
            "price": "0",
            "squareoff": "0",
            "stoploss": "0",
            "quantity": quantity
        }
        # Method 1: Place an order and return the order ID
        orderid = smartApi.placeOrder(orderparams)
        logger.info(f"PlaceOrder : {orderid}")
        print(orderid)
    except Exception as e:
        logger.exception(f"Order placement failed: {e}")
        print(e)
    except SmartApi.smartExceptions.DataException as e:
        print("error", e)
        logger.error(f"Order placement failed: {e}")
        print(e)


def cover(symbol,token,quantity,exchange):
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": symbol,
            "symboltoken": token,
            "transactiontype": "BUY",
            "exchange": exchange,
            "ordertype": "MARKET",
            "producttype": "INTRADAY",
            "duration": "DAY",
            "price": "0",
            "squareoff": "0",
            "stoploss": "0",
            "quantity": quantity
        }
        # # Method 1: Place an order and return the order ID
        orderid = smartApi.placeOrder(orderparams)
        logger.info(f"PlaceOrder : {orderid}")
        print(orderid)
    except Exception as e:
        logger.exception(f"Order placement failed: {e}")
        print(e)
    except SmartApi.smartExceptions.DataException as e:
        print("error", e)
        logger.error(f"Order placement failed: {e}")
        print(e)

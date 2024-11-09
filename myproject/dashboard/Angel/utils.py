import pandas as pd
from dashboard.Angel import AngelIntegration
import os


def get_position():
    return AngelIntegration.net_position()


def get_ltp(segment, symbol, token):
    return AngelIntegration.get_ltp(segment, symbol, token)


def sell(symbol, token, quantity, exchange):
    AngelIntegration.sell(symbol, token, quantity, exchange)


def buy(symbol, token, quantity, exchange):
    AngelIntegration.buy(symbol, token, quantity, exchange)


def BuyLmt(symbol, token, quantity, exchange, price):
    AngelIntegration.BuyLmt(symbol, token, quantity, exchange, price)


def SellLmt(symbol, token, quantity, exchange, price):
    AngelIntegration.SellLmt(symbol, token, quantity, exchange, price)


def delete_file_contents(file_name):
    try:
        # Open the file in write mode, which truncates it (deletes contents)
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        with open(file_path, 'w') as file:
            file.truncate(0)
        print(f"Contents of {file_name} have been deleted.")
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def get_api_credentials():
    credentials = {}
    delete_file_contents("OrderLog.txt")
    try:
        csv_path = os.path.join(os.path.dirname(__file__), 'Credentials.csv')
        df = pd.read_csv(csv_path)
        for index, row in df.iterrows():
            title = row['Title']
            value = row['Value']
            credentials[title] = value
    except pd.errors.EmptyDataError:
        print("The CSV file is empty or has no data.")
    except FileNotFoundError:
        print("The CSV file was not found.")
    except Exception as e:
        print("An error occurred while reading the CSV file:", str(e))

    return credentials


def get_token(symbol):
    instrument_path = os.path.join(os.path.dirname(__file__), 'Instrument.csv')
    df = pd.read_csv(instrument_path)
    row = df.loc[df['symbol'] == symbol]
    if not row.empty:
        token = row.iloc[0]['token']
        print("token: ", token)
        return token


def login_to_angel():
    credentials_dict = get_api_credentials()
    api_key = credentials_dict.get('apikey')
    username = credentials_dict.get('USERNAME')
    pwd = credentials_dict.get('pin')
    totp_string = credentials_dict.get('totp_string')

    # Call login and symbol mapping from AngelIntegration
    AngelIntegration.login(api_key=api_key, username=username, pwd=pwd, totp_string=totp_string)
    AngelIntegration.symbolmpping()

import os
from binance.client import Client
from dotenv import load_dotenv
import pandas as pd

load_dotenv() #accès aux clés API dans .env

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

client = Client(api_key, api_secret) #Instanciation de la classe client 

def get_historical_data(symbol, interval, start_date): #Interval = taille bougie. Charge les valeurs d'une paire d'actifs (symbol)
    klines = client.get_historical_klines(symbol, interval, start_date)
    df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base', 'taker_buy_quote', 'ignore'])
    df.to_csv(f"data/historical/{symbol}_{interval}.csv", index=False)

if __name__ == "__main__": #Exemple-test executé que si ce fichier est executé directement 
    get_historical_data('BTCUSDT', Client.KLINE_INTERVAL_1DAY, "1 Jan, 2022")

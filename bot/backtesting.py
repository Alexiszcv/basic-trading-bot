import pandas as pd
from strategies.rsi_strategy import rsi_strategy

def backtest(data):
    strategy_data = rsi_strategy(data) #Crée un df augmenté des signaux "buy", "sell" ou "hold"
    # Logique simple pour le backtesting
    portfolio_value = 1000  # Hypothèse de départ
    position = None #aucune position d'ouverte 

    for i in range(len(strategy_data)):
        if strategy_data['signal'][i] == 'buy' and position is None: #Si aucune position n'est ouverte et que le signal en clôture de bougie est "buy" alors on achète
            position = portfolio_value / float(strategy_data['close'][i]) #Quantité achetée
            print(f"Buying at {strategy_data['close'][i]}")
        elif strategy_data['signal'][i] == 'sell' and position is not None:
            portfolio_value = position * float(strategy_data['close'][i]) #Signaux de vente et positions à vendre alors on vend
            position = None
            print(f"Selling at {strategy_data['close'][i]}")

    if position is not None:
        portfolio_value = position * float(strategy_data['close'].iloc[-1]) #Valeur des positions encore ouvertes 
    
    print(f"Final Portfolio Value: {portfolio_value}")

if __name__ == "__main__":
    data = pd.read_csv('data/historical/BTCUSDT_1d.csv')
    backtest(data)

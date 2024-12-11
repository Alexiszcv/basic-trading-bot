import pandas as pd
from indicators.rsi import calculate_rsi

def rsi_strategy(data, rsi_period=14, rsi_overbought=70, rsi_oversold=30):
    data['rsi'] = calculate_rsi(data['close'], rsi_period) #Ajout d'une colonne 'rsi' au dataframe 'data'
    signals = []
    for i in range(len(data)):
        if data['rsi'][i] < rsi_oversold:
            signals.append('buy')
        elif data['rsi'][i] > rsi_overbought:
            signals.append('sell')
        else:
            signals.append('hold')
    data['signal'] = signals #Ajout d'une colone 'signal' au df 'data'
    return data

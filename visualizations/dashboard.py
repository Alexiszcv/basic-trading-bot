from indicators.rsi import calculate_rsi
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Pour executer :  streamlit run dashboard.py

# Charger les données historiques
try:
    data = pd.read_csv('../data/historical/BTCUSDT_1d.csv')
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')  # Conversion des timestamps en dates (ajuste selon ton format)
except FileNotFoundError:
    st.error("Le fichier de données historiques n'a pas été trouvé. Assurez-vous que le fichier BTCUSDT_1d.csv existe dans le répertoire data/historical/")
    st.stop()

# Afficher un graphique de bougies avec Matplotlib
st.title("Bot de Trading - Tableau de Bord")
st.write("Graphique des prix de BTC/USDT")

fig, ax = plt.subplots()
ax.plot(data['timestamp'], data['close'], label='Prix de Clôture')
ax.set_xlabel('Date')
ax.set_ylabel('Prix en USD')
ax.legend()
plt.xticks(rotation=45)  # Tourner les labels des dates pour plus de lisibilité
st.pyplot(fig)

# Afficher des indicateurs (par exemple RSI)
st.write("Indicateur RSI")
rsi_values = calculate_rsi(data['close'])  # Utilise ta fonction calculate_rsi
st.line_chart(rsi_values)

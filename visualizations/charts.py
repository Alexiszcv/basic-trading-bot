import matplotlib.pyplot as plt
import pandas as pd

def plot_charts(data):
    plt.plot(data['timestamp'], data['close'], label='Close Price')
    plt.legend()
    plt.title('Chart Value Over Time')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.show()


if __name__ == "__main__":
    data = pd.read_csv('data/historical/BTCUSDT_1d.csv')
    plot_charts(data)

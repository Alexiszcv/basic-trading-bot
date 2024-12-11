import matplotlib.pyplot as plt

def plot_portfolio(data):
    plt.plot(data['timestamp'], data['close'], label='Close Price')
    plt.legend()
    plt.title('Portfolio Value Over Time')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.show()

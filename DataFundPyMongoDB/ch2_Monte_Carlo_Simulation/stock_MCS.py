"""
Monte Carlo Simmulation and Density
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def cum_price(p, d, m, s):
    data = []
    for d in range(d):
        prob = stats.norm.rvs(loc=m, scale=s)
        price = (p * prob)
        data.append(price)
        p = price
    return data

def plot_data(entry):
    stk_price, days, mu, sigma = entry
    x = 0
    while x < 100:
        data = cum_price(stk_price, days, mu, sigma)
        plt.plot(data)
        x += 1
    plt.ylabel('Price')
    plt.xlabel('day')
    plt.title('Stock closing price')
    plt.show()

if __name__ == "__main__":
    tests = [
        [20, 200, 1.001, 0.005],
        [20, 500, 1.002, 0.005],
        [20, 200, 1.001, 0.02]
    ]
    for entry in tests:
        plot_data(entry)

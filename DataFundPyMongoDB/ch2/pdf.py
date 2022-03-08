"""
Find the optimal monthly order quantity for a type of car given that demand is
normally distributed (it must, because PDF is based on this assumption),
average demand (mu) is 200, and variation (sigma) is 30. Each car costs $25,000,
sells for $45,000, and half of the cars not sold at full price can be sold for
$30,000. Like other MCS experiments, you can modify the profit algorithm to
enhance realism.

 By suppliers , you are limited to order quantities of:

 - 160, 180, 200, 220, 240, 260, or 280.

MCS is used to find the profit for each order based on the information provided.
Demand is generated randomly for each iteration of the simulation.
Profit calculations by order are automated by running MCS for each order.
"""

from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


def str_int(s):
    val = "%.2f" % profit
    return float(val)


def pdf():

    n = 1000
    x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), num=n)
    y = norm.pdf(x)
    dic = {}
    for i, row in enumerate(y):
        dic[x[i]] = [np.random.uniform(0, row) for _ in range(n)]
    xs = []
    ys = []
    for key, vals in dic.items():
        for y in vals:
            xs.append(key)
            ys.append(y)
    plt.xlim(min(xs), max(xs))
    plt.ylim(0, max(ys)+0.02)
    plt.title('Normal PDF')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.scatter(xs, ys, c=xs, cmap="rainbow")
    plt.show()

if __name__ == "__main__":
    orders = [180, 200, 220, 240, 260, 280, 300]
    mu, sigma, n = 200, 30, 10000
    cost, price, discount = 25000, 45000, 30000
    profit_ls = []
    for order in orders:
        x = 1
        profit_val = []
        inv_cost = order * cost
        while x <= n:
            demand = round(np.random.normal(mu, sigma))
            if demand < order:
                diff = order - demand
                if diff > 0:
                    damt = round(abs(diff) / 2) * discount
                    profit = (demand * price) - inv_cost + damt
                else:
                    profit = (order * price) - inv_cost
            else:
                profit = (order * price) - inv_cost
            profit = str_int(profit)
            profit_val.append(profit)
            x += 1
        avg_profit = np.mean(profit_val)
        profit_ls.append(avg_profit)
        print('${0:,.2f}'.format(avg_profit), '(profit)',
              'for order:', order)
    max_profit = max(profit_ls)
    profit_np = np.array(profit_ls)
    max_ind = np.where(profit_np == profit_np.max())
    print('\nMaximum profit', '${0:,.2f}'.format(max_profit),
          'for order', orders[int(max_ind[0])])
    barlist = plt.bar(orders, profit_ls, width=15, color="thistle")
    barlist[int(max_ind[0])].set_color('lime')
    plt.title('Profits by Order Quantity')
    plt.xlabel('orders')
    plt.ylabel('profit')
    plt.tight_layout()
    plt.show()

    pdf()
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
if __name__ == '__main__':
    # creating a sequence of 1,000 x values between 0.01 and 0.99
    # (because probabilities must fall between 0 and 1).
    x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), num=1000)

    # Y values are created based on x values
    y1 = norm.pdf(x)
    plt.figure('PDF')
    plt.xlim(x.min()-.1, x.max()+0.1)
    plt.ylim(y1.min(), y1.max()+0.01)
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.title('Normal PDF')
    plt.scatter(x, y1, c=x, cmap="jet")
    plt.fill_between(x, y1, color="thistle")
    plt.show()
    plt.close('PDF')

    plt.figure('CDF')
    plt.xlabel('x')
    plt.ylabel('Probability')
    plt.title('Normal CDF')
    y2 = norm.cdf(x)
    plt.scatter(x, y2, c=x, cmap="jet")
    plt.show()
    plt.close('CDF')

    plt.figure('ICDF')
    plt.xlabel('Probability')
    plt.ylabel('x')
    plt.title('Normal ICDF (PPF)')
    y3 = norm.ppf(x)
    plt.scatter(x, y3, c=x, cmap="jet")
    plt.show()
    plt.close('ICDF')

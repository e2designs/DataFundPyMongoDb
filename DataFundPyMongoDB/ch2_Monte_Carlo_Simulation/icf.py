"""
Suppose you are a data scientist at Apple and your boss asks you to determine
Apple iPhone 8 failure rates so she can develop a mockup presentation for her
superiors.

For this hypothetical example, your boss expects four calculations:

  - Time it takes 5% of phones to fail
  - Time interval (range) where 95% of phones fail
  - Time where 5% of phones survive (don’t fail)
  - Time interval where 95% of phones survive.

  In all cases, report time in hours.

  From data exploration, you ascertain average (mu) failure time is 1,000 hours
  and standard deviation (sigma) is 300 hours.

  http://support.minitab.com/en-us/minitab-express/1/help-and-how-to/basic-statistics/probability-distributions/supporting-topics/basics/using-the-inverse-cumulative-distribution-function-icdf/#what-is-an-inverse-cumulative-distribution-function-icdf

"""

from scipy.stats import norm
import numpy as np


def np_rstrip(v):
    return np.char.rstrip(str(v), '.0')


def transform(t):
    one, two = round(t[0]), round(t[1])
    return (np_rstrip(one), np_rstrip(two))


if __name__ == "__main__":
    mu, sigma = 1000, 30

    print('Expected failure rates:')
    fail = np_rstrip(round(norm.ppf(0.05, loc=mu, scale=sigma)))
    print('5% fail within', fail, 'hours')

    fail_range = norm.interval(0.95, loc=mu, scale=sigma)
    lo, hi = transform(fail_range)
    print('95% fail between', lo, 'and', hi, end=' ')
    print('hours of usage')
    print('\nExpected survival rates:')
    last = np_rstrip(round(norm.ppf(0.95, loc=mu, scale=sigma)))
    print('5% survive up to', last, 'hours of usage')
    last_range = norm.interval(0.05, loc=mu, scale=sigma)
    lo, hi = transform(last_range)
    print('95% survive between', lo, 'and', hi, 'hours of usage')

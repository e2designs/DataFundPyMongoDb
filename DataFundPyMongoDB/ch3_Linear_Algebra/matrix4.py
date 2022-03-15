"""
Calculates the magnatude (distance) and direction (angle) with a single
vector and between two vectors
"""
import math
import numpy as np


def sqrt_sum_squares(ls):
    return math.sqrt(sum(map(lambda x: x*x, ls)))


def mag(v):
    return np.linalg.norm(v)


def a_tang(v):
    return math.degrees(math.atan(v[1]/v[0]))


def dist(v, w):
    return math.sqrt(((w[0]-v[0]) ** 2) + ((w[1]-v[1]) ** 2))


def mags(v, w):
    return np.linalg.norm(v - w)


def a_tangs(v, w):
    val = (w[1] - v[1]) / (w[0] - v[0])
    return math.degrees(math.atan(val))


if __name__ == "__main__":
    print('Origin (0,0) is used by default')
    a = np.array([0,4])
    print(f'Horizontal vector {str(a)}:')
    print(f'Magnitude: {sqrt_sum_squares(a)}')
    print(f'NumPY magnitude: {mag(a)}')
    print(f'direction: {round(a_tang(a))} degrees\n')

    b = np.array([5,0])
    print(f'Vertical vector {str(b)}:')
    print(f'Magnitude: {sqrt_sum_squares(b)}')
    print(f'NumPY magnitude: {mag(b)}')
    print(f'Direction: {round(a_tang(b))} degrees\n')

    v = np.array([3, 4])
    print('Single vector', str(v) + ':')
    print('Magnitude:', sqrt_sum_squares(v))
    print('NumPY magnitude:', mag(v))
    print('Direction:', round(a_tang(v)), 'degrees\n')

    v1, v2 = np.array([2, 3]), np.array([5, 8])
    print(f'Two vectors {str(v1)}  and {str(v2)}:')
    print('Magnitude', round(dist(v1, v2), 2))
    print('NumPY magnitude:', round(mags(v1, v2), 2))
    print('Direction:', round(a_tangs(v1, v2)), 'degrees\n')

    v1, v2 = np.array([0, 0]), np.array([3, 4])
    print('Use origin (0,0) as 1st vector:')
    print(f'Two vectors {str(v1)} and {str(v2)}:')
    print('Magnitude:', round(mags(v1, v2), 2))
    print('Direction:', round(a_tangs(v1, v2)), 'degrees')

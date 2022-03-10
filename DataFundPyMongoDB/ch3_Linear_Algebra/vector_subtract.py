"""
Subtracting two vectors is addition with the opposite (negation) of a vector.
So, vector a minus vector b is the same as a + (-b). The code example
demonstrates vector addition and subtraction for both 2- and 3-D vectors.

The code begins by importing the numpy library. It continues with functions
vector_add() and vector_subtract(), which add and subtract vectors respectively.
The main block begins by creating two 2-D vectors, and adding and subtracting
them. It continues by adding and subtracting two 3-D vectors. Any n-dimensional
can be added and subtracted in the same manner.
"""
import numpy as np


def vector_add(a, b):
    return np.add(a, b)


def vector_sub(a, b):
    return np.subtract(a, b)


if __name__ == "__main__":
    v1, v2 = np.array([3, -1]), np.array([2, 3])
    add = vector_add(v1, v2)
    sub = vector_sub(v1, v2)
    print('2D vectors:')
    print(v1, '+', v2, '=', add)
    print(v1, '-', v2, '=', sub)
    v1 = np.array([1, 3, -5])
    v2 = np.array([2, -1, 3])
    add = vector_add(v1, v2)
    sub = vector_sub(v1, v2)
    print('\n3D vectors:')
    print(v1, '+', v2, '=', add)
    print(v1, '-', v2, '=', sub)

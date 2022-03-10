"""
A matrix is an array of numbers. Many operations can be performed on a matrix
such as addition, subtraction, negation, multiplication, and division. The
dimension of a matrix is its size in number of rows and columns in that order.
That is, a 2 × 3 matrix has two rows and three columns. Generally, an m × n
matrix has m rows and n columns. An element is an entry in a matrix.
Specifically, an element in rowi and columnj of matrix A is denoted as ai,j.
Finally, a vector in a matrix is typically viewed as a column. So, a 2 × 3
matrix has three vectors (columns) each with two elements. This is a very
important concept to understand when performing matrix multiplication and/or
using matrices in data science algorithms.

The 1st code example creates a numpy matrix, multiplies it by a scalar ,
calculates means row- and column-wise, creates a numpy matrix from numpy arrays,
and displays it by row and element.

The code begins by importing numpy. It continues with two
functions—mult_scalar() and display(). Function mult_scalar() multiplies a
matrix by a scalar. Function display() displays a matrix by row and each element
of a row. The main block creates three vectors and adds them to numpy matrix A.
B is created by multiplying scalar 0.5 by A. Next, means for A are calculated by
column and row. Finally, numpy matrix C is created from three numpy arrays and
displayed by row and element.
"""

import numpy as np


def mult_scalar(m, s):
    matrix = np.empty(m.shape)
    m_shape = m.shape
    for i, v in enumerate(range(m_shape[0])):
        result = [x * s for x in m[v]]
        x = np.array(result[0])
        matrix[i] = x
    return matrix


def display(m):
    s = np.shape(m)
    cols = s[1]
    for i, row in enumerate(m):
        print('row', str(i) + ':', row, 'elements:', end=' ')
        for col in range(cols):
            print(row[col], end=' ')
        print()


if __name__ == "__main__":
    v1, v2, v3 = [1, 7, -4], [2, -3, 10], [3, 5, 6]
    A = np.matrix([v1, v2, v3])
    print('matrix A:\n', A)
    scalar = 0.5
    B = mult_scalar(A, scalar)
    print('\nmatrix B:\n', B)
    mu_col = np.mean(A, axis=0, dtype=np.float64)
    print('\nmean A (column-wise):\n', mu_col)
    mu_row = np.mean(A, axis=1, dtype=np.float64)
    print('\nmean A (row-wise):\n', mu_row)
    print('\nmatrix C:')
    C = np.array([[2, 14, -8], [4, -6, 20], [6, 10, 12]])
    print(C)
    print('\ndisplay each row and element:')
    display(C)

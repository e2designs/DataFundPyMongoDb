import numpy as np
"""
Suppose a company sells three types of pies—beef, chicken, and vegetable. Beef
pies cost $3 each, chicken pies cost $4 dollars each, and vegetable pies cost $2
dollars each. The vector representation for pie cost is [3, 4, 2]. You also know
sales by pie for Monday through Thursday. Beef sales are 13 for Monday, 9 for
Tuesday, 7 for Wednesday, and 15 for Thursday. The vector for beef sales is
thereby [13, 9, 7, 15]. Using the same logic, the vectors for chicken sales are
[8, 7, 4, 6] and [6, 4, 0, 3], respectively. The goal is to calculate total
sales for four days (Monday–Thursday)."""

def dot(v, w):
    return np.dot(v, w)


def display(m):
    for i, row in enumerate(m):
        print('Total sales by day in $:\n', end='')
        for v in np.nditer(row):
            print(f'${v}', end=' ')
        print()


if __name__ == "__main__":
    # Dollar amounts for pies [beef, chicken, vegetable]
    a = [3, 4, 2]
    A = np.matrix([a])
    print('Cost matrix A\nBeef, Chicken, Vegetable:\n', A)
    # Sales Monday - Thursday for beef, chicken and vegetable pies
    v1, v2, v3 = [13, 9, 7, 15], [8, 7, 4, 6], [6, 4, 0, 3]
    B = np.matrix([v1, v2, v3])
    print('\nDaily sales by item matrix B:\n', B)
    C = A.dot(B)
    print('\nDot product matrix C:\n', C, '\n')
    display(C)

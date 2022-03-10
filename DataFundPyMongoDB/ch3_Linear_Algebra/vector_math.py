"""
The code begins by importing matplotlib and numpy libraries. Library matplotlib
is a plotting library used for high quality visualization. Library numpy is the
fundamental package for scientific computing. It is a wonderful library for
working with vectors and matrices. The code continues with two
functions—vector_add() and set_up(). Function vector_add() adds two vectors.
Function set_up() sets up the figure for plotting. The main block begins by
creating two vectors and adding them. The remainder of the code demonstrates
graphically how vector addition works. First, it creates an axes() object with
an arrow representing vector a beginning at origin (0, 0) and ending at (3, -1).
It continues by adding text and a background color. Next, it creates a 2nd
axes() object with the same arrow a, but adds arrow b (vector b) starting at
(3, -1) and continuing to (2, 3). Finally, it creates a 3rd axes() object with
the same arrows a and b, but adds arrow c (a + b) starting at (0, 0) and ending
at (5, 2).
"""

import matplotlib.pyplot as plt
import numpy as np


def vector_add(a, b):
    return np.add(a, b)


def set_up():
    plt.figure()
    plt.xlim(-.05, add_vectors[0]+0.4)
    plt.ylim(-1.1, add_vectors[1]+0.4)


if __name__ == "__main__":
    v1, v2 = np.array([3, -1]), np.array([2, 3])
    add_vectors = vector_add(v1, v2)
    set_up()
    ax = plt.axes()
    ax.arrow(0, 0, 3, -1, head_width=0.1, fc="b", ec="b")
    ax.text(1.5, -0.35, 'a')
    ax.set_facecolor('honeydew')
    set_up()
    ax = plt.axes()
    ax.arrow(0, 0, 3, -1, head_width=0.1, fc="b", ec="b")
    ax.arrow(3, -1, 2, 3, head_width=0.1, fc="crimson", ec="crimson")
    ax.text(1.5, -0.35, 'a')
    ax.text(4, -0.1, 'b')
    ax.set_facecolor('honeydew')
    set_up()
    ax = plt.axes()
    ax.arrow(0, 0, 3, -1, head_width=0.1, fc="b", ec="b")
    ax.arrow(3, -1, 2, 3, head_width=0.1, fc="crimson", ec="crimson")
    ax.arrow(0, 0, 5, 2, head_width=0.1, fc="springgreen", ec="springgreen")
    ax.text(1.5, -0.35, 'a')
    ax.text(4, -0.1, 'b')
    ax.text(2.3, 1.2, 'a + b')
    ax.text(4.5, 2.08, add_vectors, color="fuchsia")
    ax.set_facecolor('honeydew')
    plt.show()

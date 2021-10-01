import numpy as np
import matplotlib.pyplot as plt
from math import *

# The Function we Solve
def f(x):
    y = x**4 + 2*x**3 - 5*x**2 - 7*x - 5
    return y

# (a,b): the interval we suspect to find the root
# N: number of repetitions
def RegulaFalsi(a, b, N):

    for i in range(N):
        y = (f(b)*a-f(a)*b)/(f(b)-f(a))
        if np.sign(f(a))*np.sign(f(y)) == -1: b = y
        else: a = y

    solution = y

    return solution

if __name__ == '__main__':

    # Visualize the Function
    x = np.linspace(1,3,100)
    y = f(x)

    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout
    plt.show()

    print(RegulaFalsi(1.5,3,30))
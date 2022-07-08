import numpy as np
import matplotlib.pyplot as plt
from math import *

# The Function we Solve
def f(x):
    y = x**4 + 2*x**3 - 5*x**2 - 7*x - 5
    return y

# x0: where we begin (first guess)
# x1: second guess
# N: number of repetitions
def Secant(x0, x1, N):

    for i in range(N):
        x = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0 = x

    solution = x

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

    print(Secant(1.5, 3,30))

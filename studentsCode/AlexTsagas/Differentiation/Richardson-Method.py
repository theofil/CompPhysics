import numpy as np
import matplotlib.pyplot as plt
from math import *

# Function
def f(x):
    return exp(x)

# To compute the first column of Richardson method
def ThreeMidpoint(x0, h):
    df = (f(x0+h)-f(x0-h))/(2*h)
    return df


def Richarson(x0, h, tol):
    R = np.zeros((50,50))

    R[1][1] = ThreeMidpoint(x0, h)

    for i in range(2, 50):
        h = 0.5*h
        R[i][1] = ThreeMidpoint(x0, h)

        for j in range(2, i+1):
            R[i][j] = R[i][j-1] + (1/(pow(4,j-1) - 1)) * (R[i][j-1] - R[i-1][j-1])

        if abs((R[i][i] - R[i-1][i-1])) < tol: break

    return R[i][i]

if __name__ == '__main__':

    x = 0

    print(Richarson(x, 1, 0.01))

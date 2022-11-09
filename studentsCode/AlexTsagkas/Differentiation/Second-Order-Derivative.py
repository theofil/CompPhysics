import numpy as np
import matplotlib.pyplot as plt
from math import *

# Function
def f(x):
    return exp(x)

# Compute the Second Derivative of f(x) at x0 with step h
def SecondOrder(x0, h):
    ddf = (f(x0-h) - 2*f(x0) + f(x0+h))/(h**2)
    return ddf

if __name__ == '__main__':

    x = 0

    print(SecondOrder(x, 0.01))

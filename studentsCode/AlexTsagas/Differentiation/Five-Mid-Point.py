import numpy as np
import matplotlib.pyplot as plt
from math import *

# Function
def f(x):
    return exp(x)

# Compute Derivative of f(x) at x0 with step h
def FiveEndPoint(x0, h):
    df = (-25*f(x0) + 48*f(x0+h) - 36*f(x0+2*h) + 16*f(x0+3*h) - 3*f(x0+4*h))/(12*h)
    return df

if __name__ == '__main__':

    x = 0

    print(FiveEndPoint(x, 0.01))

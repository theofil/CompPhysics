import numpy as np
import matplotlib.pyplot as plt
from math import *

# Function
def f(x):
    return exp(x)

# Compute Derivative of f(x) at x0 with step h
def ThreeMidpoint(x0, h):
    df = (f(x0+h)-f(x0-h))/(2*h)
    return df

if __name__ == '__main__':

    x = 0

    print(ThreeMidpoint(x, 0.01))

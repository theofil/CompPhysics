import numpy as np
from math import *

# Function
def f(x):
    y = 1 / sqrt(2 * np.pi) * exp(-x ** 2 / 2)
    return y

# General Gauss Method with Five Points
def GaussQuad5(a, b, tol):

    # Compute Integral with 5 Point Gauss Method
    def GaussQuad(a, b):
        t = [-1/3*sqrt(5+2*sqrt(10/7)), -1/3*sqrt(5-2*sqrt(10/7)), 0,
             1/3*sqrt(5-2*sqrt(10/7)), 1/3*sqrt(5+2*sqrt(10/7))]

        x = np.zeros(5)

        for i in range(5):
            x[i] = 0.5*((b-a)*t[i] + b+a)

        w = [(322 + 13*sqrt(70))/900, (322 - 13*sqrt(70))/900, 128/225,
             (322 + 13*sqrt(70))/900, (322 - 13*sqrt(70))/900]

        I = 0.0

        for i in range(5):
            I += 0.5*(b-a)*w[i]*f(x[i])

        return I

    # We compute the Integral in N intervals using Gauss Method so as to Compute Integral Error
    def GaussQuadn(n):
        h = (b - a) / n
        I = 0.0

        for i in range(n):
            x0 = a + i * h
            x1 = x0 + h
            I += GaussQuad(x0, x1)

        return I

    # We compute the error using analytic computations
    def dGaussQuadn(n):
        h = (b - a) / (2 * n)
        I2 = 0.0

        for i in range(2 * n):
            x0 = a + i * h
            x1 = x0 + h
            I2 += GaussQuad(x0, x1)

        dI = 32 / 31 * abs(I2 - GaussQuadn(n))

        return dI

    # Min Value for Gauss Method
    n = 2 
    # General Error
    η = dGaussQuadn(n) / GaussQuadn(n)

    while η > tol:
        n += 1
        η = dGaussQuadn(n) / GaussQuadn(n)

    return GaussQuadn(n), dGaussQuadn(n), η

if __name__ == "__main__":
    print('\nCimputated with 5 Point Gauss Method:')
    print(f"\tI ± δI = {GaussQuad5(-5, 5, 0.001)[0]:.8f} ± {GaussQuad5(-5, 5, 0.001)[1]:.8f}")
    print(f'\tΗ σχετική ακρίβεια είναι η = {GaussQuad5(-5, 5, 0.001)[2]:.8f} < 0.1 %')
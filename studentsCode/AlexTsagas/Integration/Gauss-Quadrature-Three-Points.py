import numpy as np

#  Function
def f(x):
    y = 1 /np.sqrt(2 * np.pi) * np.exp(-x ** 2 / 2)
    return y

# General Gauss method with three points
def GaussQuad3(a, b, tol):
    # Compute Integral with 3 Point Gauss Method
    def GaussQuad(a, b):
        t = [-pow(3/5, 0.5), 0, pow(3/5, 0.5)]
        x = [0.5*((b-a)*t[0] + b+a), 0.5*((b-a)*t[1] + b+a),
             0.5*((b-a)*t[2] + b+a)]
        I = 0.5 * (b - a) * (f(x[0])/1.8 + f(x[1])/1.125 + f(x[2])/1.8)
        return I

    # We compute the Integral in N Intervals Using Gauss Method so as to Compute the Error
    def GaussQuadn(n):
        h = (b-a)/n
        I = 0.0

        for i in range(n):
            x0 = a + i*h
            x1 = x0 + h
            I += GaussQuad(x0, x1)

        return I

    # We compute the error using analytic computations
    def dGaussQuadn(n):
        h = (b-a)/(2*n)
        I2 = 0.0

        for i in range(2*n):
            x0 = a + i*h
            x1 = x0 + h
            I2 += GaussQuad(x0, x1)

        dI = 32/31 * abs(I2-GaussQuadn(n))

        return dI

    # Min Value
    n = 2
    # General Error
    η = dGaussQuadn(n)/GaussQuadn(n)

    while η > tol:
        n += 1
        η = dGaussQuadn(n)/GaussQuadn(n)

    return GaussQuadn(n), dGaussQuadn(n), η

if __name__ == "__main__":
    print('\nComputed with 3 Point Gauss Method:')
    print(f"\tI ± δI = {'%.8f'%GaussQuad3(-5, 5, 0.001)[0]} ± {GaussQuad3(-5, 5, 0.001)[1]:.8f}")
    print(f'\tThe General Error is η = {GaussQuad3(-5, 5, 0.001)[2]:.5f} < 0.1 %')
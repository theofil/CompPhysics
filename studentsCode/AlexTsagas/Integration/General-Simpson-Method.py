import numpy as np

# Function
def f(x):
    y = 1 / np.sqrt(2 * np.pi) * np.exp(-x ** 2 / 2)
    return y

# General Simpson Method
def Simpson(a, b, tol):
    # Integral Cimputations With Simpson Method
    def S(n):
        h = (b-a)/(2*n)
        I = h/3*(f(a) + f(b))

        for i in range(1, 2*n):
            x_i = a + h*i
            if i % 2 == 0:
                I += 2*h/3 * f(x_i)
            else:
                I += 4*h/3 * f(x_i)

        return I

    # Integral Error
    def dS(n):

        dI = (np.abs(S(2*n) - S(n))) / 15

        return dI

    # min{n} = 3 in General Simpson Method
    n = 3 
    d = dS(n)/S(n)

    while d > tol:
        n += 1
        d = dS(n)/S(n)

    return S(n), dS(n), d

if __name__ == "__main__":
    print('\nComputated with General Simpson Method:')
    print(f"\tI ± δI = {Simpson(-5, 5, 0.001)[0]:.8f} ± {Simpson(-5, 5, 0.001)[1]:.8f}")
    print(f'\tThe Relative error is η = {Simpson(-5, 5, 0.001)[2]:.4f} < 0.1 %')
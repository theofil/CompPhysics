import numpy as np

# Funciton
def f(x):
    y = 1 / np.sqrt(2 * np.pi) * np.exp(-x ** 2 / 2)
    return y

# Adaptable Simpson Method
def adSimpson(a, b, tol):

    # Simpson Rule for 2 intervals
    def S(n, m):
        value = (m-n)/6 * (f(n) + f(m) + 4*f(0.5*(n + m)))
        return value

    # Compute Integral with Simpson Rule in left half and right hald interval
    Il, Ir = S(a, 0.5*(a+b)), S(0.5*(a+b), b)
    # Compute Integral wth Simpson Rule
    I = S(a, b)

    # Integral Error
    dI = np.abs((I - (Il+Ir)))/15

    # Check If We Get the Desired Tolerance
    if dI < tol:
        I = Il + Ir
    # If we Don't get it Reiterate
    else:
        Il = adSimpson(a, 0.5*(a+b), 0.5*tol)
        Ir = adSimpson(0.5*(a+b), b, 0.5*tol)

    I = Il + Ir

    return I

if __name__ == "__main__":
    print('\nComputed with Adaptable Simpson Method:')
    print(f'\tI = {adSimpson(-5, 5, 0.001):.8f}')

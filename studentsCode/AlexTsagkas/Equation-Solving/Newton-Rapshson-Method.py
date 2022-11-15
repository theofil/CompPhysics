import numpy as np
import matplotlib.pyplot as plt

# The function we Want to Solve
def f(x):
    return np.tan(x) - x / (1 - x**2)

if __name__ == "__main__":

    # Plot the Function to Visualize the Root
    x = np.linspace(2,4.5,1000)
    y = f(x)

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.tight_layout
    plt.show()

    # Derivative of f(x)
    def df(x):
        return 1 / np.cos(x) ** 2 - (1 + x ** 2) / (1 - x ** 2) ** 2

    # Retroactive Newton-Rapshon Relation
    def g(xn):
        return xn - f(xn) / df(xn)
    
    # Where it Begins
    x0 = 3.0

    # Loop
    for i in range(7):
        x = g(x0)
        x0 = x
    
    root = x

    print(f'The root of f is: x = {root:.4f}.')
    print(f'The valus of f for the above x is {f(root):.16f}.')

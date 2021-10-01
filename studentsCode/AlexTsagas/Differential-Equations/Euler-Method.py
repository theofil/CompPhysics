import numpy as np
from math import *
import matplotlib.pyplot as plt

''' The problem is: dy/dt = f(t,y).'''

def f(t, y):
    return 0.5*y

# a,b: edges of the interval, w0:ititial value, h:step
def Euler(a, b, w0, h):
    n = ceil((b-a)/h)

    w, t = np.zeros(n+1), np.zeros(n+1)
    w[0], t[0] = w0, a

    for i in range(n):
        w[i+1] = w[i] + h*f(t[i], w[i])
        t[i+1] = t[i] + h

    return w, t

if __name__ == '__main__':

    a, b, w0, h = 0, 2, 1, 0.2

    print(Euler(a, b, w0, h)[0])

    # Visualization
    x = np.linspace(0, 2, 100)

    y = np.zeros(len(x))

    for j in range(len(x)):
        y[j] = exp(0.5*x[j])

    plt.plot(x, y, color="black", label="Solution")
    plt.plot(Euler(a, b, w0, h)[1], Euler(a, b, w0, h)[0], label="Euler")
    plt.xlabel("t")
    plt.ylabel("y")
    plt.legend()
    plt.show()

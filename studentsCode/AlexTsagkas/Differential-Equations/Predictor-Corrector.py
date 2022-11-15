import numpy as np
from math import *
import matplotlib.pyplot as plt

''' The problem is: dy/dt = f(t,y).'''

def f(t, y):
    return 0.5*y

# a,b: edges of the interval, w0:ititial value, h:step
def PredictorCorrector(a, b, w0, h):
    n = ceil((b - a) / h)

    w, t = np.zeros(n+1), np.zeros(n+1)
    w[0], t[0] = w0, a

    for i in range(3):
        k1 = h * f(t[i], w[i])
        k2 = h * f(t[i] + h / 2, w[i] + k1 / 2)
        k3 = h * f(t[i] + h / 2, w[i] + k2 / 2)
        k4 = h * f(t[i] + h, w[i] + k3)
        w[i+1] = w[i] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        t[i+1] = t[i] + h

    for i in range(3, n):
        #Predictor
        w[i+1] = w[i] + h/24*(55*f(t[i], w[i]) - 59*f(t[i-1], w[i-1]) + 37*f(t[i-2], w[i-2]) - 9*f(t[i-3], w[i-3]))
        #Corrector
        w[i+1] = w[i] + (h/24)*(9*f(t[i+1], w[i+1]) + 19*f(t[i], w[i]) - 5*f(t[i-1], w[i-1]) + f(t[i-2], w[i-2]))

        t[i+1] = t[i] + h

    return w, t

if __name__ == '__main__':

    a, b, w0, h = 0, 2, 1, 0.2

    print("\n", PredictorCorrector(a, b, w0, h)[0])

    # Visualization
    x = np.linspace(0, 2, 100)

    y = np.zeros(len(x))

    for j in range(len(x)):
        y[j] = exp(0.5*x[j])

    plt.plot(x, y, color="black", label="Solution")
    plt.plot(PredictorCorrector(a, b, w0, h)[1], PredictorCorrector(a, b, w0, h)[0], label="Predictor-Corrector")
    plt.xlabel("t")
    plt.ylabel("y")
    plt.legend()
    plt.show()

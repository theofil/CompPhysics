import numpy as np
import matplotlib.pyplot as plt

# Qubic Splines Method
def CubicSplines(x_data, f_data, x):
    n = len(x_data)
    a, b, c, d = f_data, np.zeros(n), np.zeros(n), np.zeros(n)

    # Intervals
    h = np.zeros(n)
    for i in range(n-1):
            h[i] = x_data[i+1] - x_data[i]

    def SystemSolver():
        A, B, X = np.zeros((n, n)), np.zeros((n, 1)), np.zeros((n, 1))
        # AX = B and we look for X = c

        # Array A
        for row in range(1, n - 1):
            for col in range(n):
                if col == row - 1:
                    A[row][col] = h[row - 1]
                elif col == row:
                    A[row][col] = 2 * (h[row - 1] + h[row])
                elif col == row + 1:
                    A[row][col] = h[row]
        A[0][0], A[n - 1][n - 1] = 1.0, 1.0

        # Array B
        for row in range(1, n - 1):
            B[row] = 3 * (a[row + 1] - a[row]) / h[row] - 3 * (a[row] -
                     a[row - 1]) / h[row - 1]
        B[0][0], B[n - 1][0] = 0.0, 0.0

        # Gauss - Siedel
        N = 200  # Iterations

        for i in range(N):
            for row in range(n):
                U = X.copy()  # clone of X with zerod the X[row]
                              # element
                U[row] = 0
                X[row] = (B[row] - A[row] @ U)/A[row, row]

        return X

    c = SystemSolver()

    for i in range(n-1):
        b[i] = (a[i+1] - a[i])/h[i] - h[i]*(c[i+1] + 2*c[i])/3.0

    for i in range(n-1):
        d[i] = (c[i+1] - c[i])/(3.0*h[i])

    def Spline():
        S = 0.0

        for i in range(n-1):
            if x >= x_data[i] and x <= x_data[i + 1]:
                S = a[i] + b[i]*(x - x_data[i]) + \
                    c[i]*pow(x - x_data[i], 2) + \
                    d[i]*pow(x - x_data[i], 3)

        return S

    return Spline()

if __name__ == "__main__":
    # Some Data
    x_data = [-1.6, -1.0, -0.4, 0.2, 0.8, 1.4]
    f_data = [0.278037, 0.606531, 0.923116, 0.980199, 0.726149, 0.375311]

    print('\nComputated with Cubic Splines Method:')
    print(f'\tf(0) = {CubicSplines(x_data, f_data, 0)[0]:.8f}')
    print(f'\tf(1) = {CubicSplines(x_data, f_data, 1)[0]:.8f}')

    x = np.linspace(-1.6, 1.4, 150)
    y = np.zeros(len(x))
    i = 0

    for point in x:
        y[i] += CubicSplines(x_data, f_data, point)
        i += 1

    plt.subplot(1, 1, 1)
    plt.plot(x, y, linewidth=1, color = 'cyan', label='Cubic Splines')
    plt.scatter(x_data, f_data, color='black', marker = ".", label='Sample Points')

    plt.legend(loc='lower center', prop={'size': 12})
    plt.ylabel('$y$')
    plt.xlabel('$x$')
    plt.title('Cubic Splines Method')

    plt.tight_layout()
    plt.show()

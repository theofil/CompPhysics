import numpy as np
import matplotlib.pyplot as plt

# Nenille Method
def Q(x):
    n = len(x_data)
    Q = np.zeros((n,n))

    for i in range(0, n):
        Q[i][0] = f_data[i]

        for j in range(1, i+1):
            Q[i][j] = ((x - x_data[i-j]) * Q[i][j-1] - (x - x_data[i]) * Q[i-1][j-1]) / (x_data[i] - x_data[i-j])

    return Q[i][i]

if __name__ == "__main__":
    # Some Data
    x_data = [-1.6, -1.0, -0.4, 0.2, 0.8, 1.4]
    f_data = [0.278037, 0.606531, 0.923116, 0.980199, 0.726149, 0.375311]

    print('\nComputated with Neville Method:')
    print(f'\tf(0) = {Q(0):.6f}')
    print(f'\tf(1) = {Q(1):.6f}')

    # Visualize Neville Polynomial
    x = np.linspace(-1.6, 1.4, 150)
    y = np.zeros(len(x))

    i = 0

    for point in x:
        y[i] += Q(point)
        i += 1

    plt.subplot(1, 1, 1)
    plt.plot(x, y, linewidth = 1, color = 'magenta', label = 'Neville Polynomial')
    plt.scatter(x_data, f_data, color = 'black', marker = ".", label = 'Sample Points')

    plt.legend(loc = 'lower center', prop = {'size': 12})
    plt.ylabel('$y$')
    plt.xlabel('$x$')
    plt.title('Mέθοδος Neville')
    plt.show()

from matplotlib import markers
import numpy as np
import matplotlib.pyplot as plt

# Langrange Polynomial of n^th Degree - The Degree is Specified by the Data we Use
def P(x_data, f_data, pos, x):  # pos is an array with elements the positions of x_data we use

    # n = Degree of the polynomial + 1
    n = len(pos)

    def L(x_data, pos, x):

        L = np.ones(n)

        # Polynomial that goes through x_data[pos[i]]
        for i in range(n):
            for j in range(n):
                if pos[i] != pos[j]:
                    L[i] *= (x - x_data[pos[j]]) / (x_data[pos[i]] - x_data[pos[j]])
        return L

    P = 0.0

    for i in range(n):
            P += f_data[pos[i]] * L(x_data, pos, x)[i]

    return P

# Function to Generate Points for Graphs
def graph(pos, n = 150):
    x_graph = np.linspace(x_data[np.amin(pos)], x_data[np.amax(pos)], n)
    y_graph = np.zeros(len(x_graph))

    i = 0

    for x in x_graph:
        y_graph[i] += [P(x_data, f_data, pos, x)]
        i += 1

    return x_graph, y_graph

if __name__ == "__main__":
    # Some Data
    x_data = [-1.6, -1.0, -0.4, 0.2, 0.8, 1.4]
    f_data = [0.278037, 0.606531, 0.923116, 0.980199, 0.726149, 0.375311]

    print('\nCompuated with Lagrange Polynomials of 3^rd Degree:')
    print(f'\tf(0) = {P(x_data, f_data, [1, 2, 3, 4], 0):.6f}')
    print(f'\tf(1) = {P(x_data, f_data, [2, 3, 4, 5], 1):.6f}')

    print('\nCompuated with Lagrange Polynomials of 4^th Degree:')
    print(f'\tf(0) = {P(x_data, f_data, [1, 2, 3, 4, 5], 0):.6f}')
    print(f'\tf(1) = {P(x_data, f_data, [1, 2, 3, 4, 5], 1):.6f}')

    # Visualize the Lagrange Polynomials
    plt.subplot(1, 1, 1)
    plt.plot(graph([1, 2, 3, 4])[0], graph([1, 2, 3, 4])[1], linewidth = 1, label = 'Third Degree with pos = [1, 2, 3, 4]')
    plt.plot(graph([2, 3, 4, 5])[0], graph([2, 3, 4, 5])[1], linewidth = 1, label = 'Third Degree with pos = [2, 3, 4, 5]')
    plt.plot(graph([1, 2, 3, 4, 5])[0], graph([1, 2, 3, 4, 5])[1], linewidth = 1, label = 'Fourth Degree with pos = [1, 2, 3, 4, 5]')
    plt.scatter(x_data, f_data, color = 'black', marker = ".", label = 'Sample Points')

    plt.legend(loc = 'lower center', prop = {'size': 10})
    plt.ylabel('$y$')
    plt.xlabel('$x$')
    plt.title('Lagrange Method')
    plt.show()

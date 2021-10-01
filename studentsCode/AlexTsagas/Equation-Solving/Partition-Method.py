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

    # Repetitions
    N = 20

    # Region Edges (Find Them in the Diagram of the Function)
    a, b = [2], [4]

    # Counters
    i, j = 0, 0

    for n in range(N):
        # Center of Interval (a,b)
        c = 0.5 * (a[i] + b[j])
        # Where is the Root? In (a,c) or in (c,b)? (Bolzano Theorem)
        if np.sign(f(a[i])) * np.sign(f(c)) == -1.0:
            b += [c]
            j += 1
        elif np.sign(f(c)) * np.sign(f(b[j])) == -1.0:
            a += [c]
            i += 1

    # We Specify the Root as the Center of the Interval (a,b)
    root = 0.5 * (b[j] + a[i])

    print(f'The root of f is: x = {root:.4f}.')
    print(f'The valus of f for the above x is {f(root):.7f}.')

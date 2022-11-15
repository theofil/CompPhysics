import numpy as np

# Function
def f(x):
    y = 1 / np.sqrt(2 * np.pi) * np.exp(-x ** 2 / 2)
    return y

# General Romberg Method
def Romberg(a, b, tol):
    R = np.zeros((50, 50))
    h = b - a

    # We compute the first column of Romberg array with Trapezoid Method
    R[1][1] = 0.5*h*(f(a) + f(b))

    for i in range(2, 50+1):
        R[i][1] = 0.5*R[i-1][1]

        for k in range(1, int(pow(2, i-2)+1)):
            R[i][1] += 0.5 * h * f(a + (k-0.5)*h)

        # There we start computing elements from the other columns
        for j in range(2, i+1):
            R[i][j] = R[i][j-1] + (1./(pow(4, j-1)-1))*(R[i][j-1] - R[i-1][j-1])

        d = np.abs((R[i][i]-R[i-1][i-1])/R[i][i])

        if(d < tol):
            break

        h = 0.5 * h

    I = R[i][j]
    dI = d * I

    return I, dI, d

if __name__ == "__main__":
    print('\nComputated with General Romberg Method:')
    print(f"\tI ± δI = {Romberg(-5, 5, 0.001)[0]:.8f} ± {Romberg(-5, 5, 0.001)[1]:.8f}")
    print(f'\tThe relative error is η = {Romberg(-5, 5, 0.001)[2]:.5f} < 0.1 %')

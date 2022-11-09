import numpy as np

# Random Number Generator - Uniform Distribution
def U():
        return np.random.rand()

# Integrated Function
def f(x):
    return np.exp(x)

if __name__ == "__main__":
    # Number of Random Numbers
    N = 1000
    # sample_mean(f)
    μf = 0
    # sample_mean(f^2) 
    μf2 = 0
    # Inegral computated with Crude-Monte-Carlo Method
    I_sample = 0

    # Limits of Integration
    a, b = 0, 10
    # "Volume" of Integration
    V = (b-a)

    for i in range(N):
        xi = V * U() + a

        μf += f(xi)/N
        μf2 += f(xi)**2/N

    I_sample = V * μf

    # Variance of f(x)
    σf_sample = np.sqrt((N/(N-1)) * (μf2 - μf**2))

    # Integral Error
    δI_sample = V/np.sqrt(N)*σf_sample

    # Integral Relative Error
    η_sample = δI_sample/I_sample

    print(f'I ± δI = {I_sample:.2f} ± {δI_sample:.2f},\nη_sample = {η_sample:.3f}')

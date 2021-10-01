import numpy as np
import matplotlib.pyplot as plt 

# We Will Solve the Diff Equation: dA/dt = -λA = f(A,t), 0<=t<=8 [s]
def f(t, A):
    λ = np.log(2)/2 # Constant
    f = -λ*A
    return f

# Second Order Runge Kutta Method (τ: the step)
def RK2(τ):
    # Interval Edges
    a, b = 0, 8
    # Number of Repetitions
    N = int((b-a)/τ)

    w = np.zeros(N+1)
    t = np.zeros(N+1)

    # Starting Points
    w[0], t[0] = 1, 0

    for i in range(N):
        w[i+1] = w[i] + τ * f(t[i] + τ/2, w[i] + τ/2*f(t[i],w[i]))
        t[i+1] = t[i] + τ

    return w, t

# We Compute the Uncertenty
def unc_RK2(τ):
    unc = np.zeros(11)
    rk2_τ, rk2_2τ = RK2(τ)[0], RK2(τ/2)[0]

    for i in range(1,11):
        unc[i] = (rk2_τ[i]-rk2_2τ[2*i])/3

    return unc

if __name__ == '__main__':

    w_rk2, t_rk2, unc_rk2 = RK2(0.8)[0], RK2(0.8)[1], unc_RK2(0.8)

    print('\nComputed with 2^nd Order Runge Kutta Method:')
    for i in range(11):
        print(f"\tStep {i} with t_{i}={t_rk2[i]:.1f}: {w_rk2[i]:.8f} ± {unc_rk2[i]:.8f}")

    # Visualize the Results
    ## Plot the Solutions for Both Methods
    plt.plot(t_rk2, w_rk2, color='black', marker=".", linewidth=1, label='Runge Kutta 2th Order')

    ## How Graph is Shown (legend, axis titles, graph title)
    plt.legend(loc='upper center', prop={'size': 10})
    plt.ylabel('A(t) [kBq]')
    plt.xlabel('Time [s]')
    plt.title('Solution of Differential Equation')

    ## Show the major grid lines with dark grey lines
    plt.grid(b=True, which='major', color='#666666', linestyle='--')

    ## Show the minor grid lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.2)

    ## Fix Quality
    plt.tight_layout()

    ## Show the Graph
    plt.show()

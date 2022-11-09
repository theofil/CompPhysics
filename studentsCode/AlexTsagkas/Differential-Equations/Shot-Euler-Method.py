import numpy as np
import matplotlib.pyplot as plt

# Write with LaTeX
from matplotlib import rc
rc('text', usetex=True)
rc('font', family='serif')

# State the Problem

''' We will solve the problem of throwing a point-like sphere with initial position:

(x_o, y_o) = (0 [m], 0 [m]) ,

initial velocity:

v_o = 20 [m/s]

and throwing angle:

phi = pi/6 [rad]. '''

''' So the problem is seperated to the following:

1. dv_x/dt = 0 = func_v_x(t, x, y, v_x, v_y),
2. dv_y/dt = -g = func_v_y(t, x, y, v_x, v_y),
3. dx/dt = v_x = func_x(t, x, y, v_x, v_y),
4. dy/dt = v_y = func_y(t, x, y, v_x, v_y). '''

def func_x(t, x, y, v_x, v_y):
    return v_x

def func_v_x(t, x, y, v_x, v_y):
    return 0

def func_y(t, x, y, v_x, v_y):
    return v_y

def func_v_y(t, x, y, v_x, v_y):
    g = 10 # Gravitational Intensity Near Earth
    return -g

def shot_Euler(τ):

    # τ : Time Step
    t = np.zeros(200)

    y, v_y = np.zeros(200), np.zeros(200)
    x, v_x = np.zeros(200), np.zeros(200)

    # Errors
    e_x, e_y = np.zeros(200), np.zeros(200)

    # Initial Conditions
    t[0] = 0
    y[0], v_y[0] = 0, 10
    x[0], v_x[0] = 0, 10 * np.sqrt(3)

    i = 0 # Counter
    while y[i-1] >= 0:
        # x - Direction
        x[i+1] = x[i] + τ*func_x(t, x, y, v_x, v_y)[i]
        v_x[i+1] = v_x[i] + τ*func_v_x(t[i], x[i], y[i], v_x[i], v_y[i])
        # y - Direction
        y[i+1] = y[i] + τ*func_y(t, x, y, v_x, v_y)[i]
        v_y[i+1] = v_y[i] + τ*func_v_y(t[i], x[i], y[i], v_x[i], v_y[i])
        # Time
        t[i+1] = t[i] + τ

        # Errors
        e_x[i] = 10*np.sqrt(3)*t[i] - x[i]
        e_y[i] = -5*t[i]**2 + 10*t[i] - y[i]
        # Counter
        i += 1

    # We Kepp Values != 0 for x and y respectively
    y, x = y[:i], x[:i]
    t = t[:i]
    e_x, e_y = e_x[:i], e_y[:i]

    return x, y, t, e_x, e_y

if __name__ == '__main__':


    Exy, (Ex, Ey) = plt.subplots(1, 2)

    Exy.suptitle(r'Results from Euler Method')

    Ex.plot(shot_Euler(0.05)[2], shot_Euler(0.05)[0], color='black', linewidth=1)
    # How Graph is Shown (axis titles)
    Ex.set_ylabel(r'$x(t)$ $[m]$')
    Ex.set_xlabel(r'$t$ $[s]$')
    # Show the major grid lines
    Ex.grid(b=True, which='major', color='#666666', linestyle='--')
    # Show the minor grid lines
    Ex.minorticks_on()
    Ex.grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.1)

    Ey.plot(shot_Euler(0.05)[2], shot_Euler(0.05)[1], color='red', linewidth=1)
    # How Graph is Shown (axis titles)
    Ey.set_ylabel(r'$y(t)$ $[m]$')
    Ey.set_xlabel(r'$t$ $[s]$')
    # Show the major grid lines
    Ey.grid(b=True, which='major', color='#666666', linestyle='--')
    # Show the minor grid lines
    Ey.minorticks_on()
    Ey.grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.1)

    # Fix Quality
    Exy.tight_layout()
    #Save the Graph
    Exy.savefig('Euler-Method-Results.pdf')

    Eexyt, (Eext, Eeyt) = plt.subplots(1, 2)

    Eexyt.suptitle('Erros from Euler Method with Respect to Time')

    Eext.plot(shot_Euler(0.05)[2], shot_Euler(0.05)[3], color='b', linewidth=1)
    # How Graph is Shown (axis titles)
    Eext.set_ylabel(r'$e_x(t)$ $[m]$')
    Eext.set_xlabel(r'$t$ $[s]$')
    # Show the major grid lines
    Eext.grid(b=True, which='major', color='#666666', linestyle='--')
    # Show the minor grid lines
    Eext.minorticks_on()
    Eext.grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.1)

    Eeyt.plot(shot_Euler(0.05)[2], shot_Euler(0.05)[4], color='m', linewidth=1)
    # How Graph is Shown (axis titles)
    Eeyt.set_ylabel(r'$e_y(t)$ $[m]$')
    Eeyt.set_xlabel(r'$t$ $[s]$')
    # Show the major grid lines
    Eeyt.grid(b=True, which='major', color='#666666', linestyle='--')
    # Show the minor grid lines
    Eeyt.minorticks_on()
    Eeyt.grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.1)

    # Fix Quality
    Eexyt.tight_layout()
    #Save the Graph
    Eexyt.savefig('Erros-with-Respect-to-Time.pdf')

    # Sfalmata Synarthsei toy τ (Bhma)
    Eulere_x, Eulere_y = np.zeros(200), np.zeros(200)
    bhma = np.linspace(0.02, 1, 100)

    i = 0  # Metrhths
    for τ in bhma:
        Eulere_x[i] = shot_Euler(τ)[3][-1]
        Eulere_y[i] = shot_Euler(τ)[4][-1]
        i += 1

    Eulere_x = Eulere_x[:i]
    Eulere_y = Eulere_y[:i]

    Eexyτ, (Eexτ, Eeyτ) = plt.subplots(1, 2)

    Eexyτ.suptitle('Erros from Euler Method with Respect to Time Step')

    Eexτ.plot(bhma, Eulere_x, color='g', linewidth=1)
    # How Graph is Shown (axis titles)
    Eexτ.set_ylabel(r'$e_x(\tau)$ $[m]$')
    Eexτ.set_xlabel(r'$\tau$ $[s]$')
    # Show the major grid lines
    Eexτ.grid(b=True, which='major', color='#666666', linestyle='--')
    # Show the minor grid lines
    Eexτ.minorticks_on()
    Eexτ.grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.1)

    Eeyτ.plot(bhma, Eulere_y, color='c', linewidth=1)
    # How Graph is Shown (axis titles)
    Eeyτ.set_ylabel(r'$e_y(\tau)$ $[m]$')
    Eeyτ.set_xlabel(r'$\tau$ $[s]$')
    # Show the major grid lines
    Eeyτ.grid(b=True, which='major', color='#666666', linestyle='--')
    # Show the minor grid lines
    Eeyτ.minorticks_on()
    Eeyτ.grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.1)

    # Fix Quality
    Eexyτ.tight_layout()
    #Save the Graph
    Eexyτ.savefig('Erros-with–Respect-to-Time-Step.pdf')

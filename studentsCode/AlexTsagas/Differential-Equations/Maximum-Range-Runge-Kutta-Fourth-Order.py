import numpy as np
from math import *
import matplotlib.pyplot as plt

# Write with LaTeX
from matplotlib import rc
rc('text', usetex=True)
rc('font', family='serif')

# State the Problem

''' We will save a graph of range with respect to shot angle, so as to approximate the optimum shot angle. The problem is stated below:

d^2\vec{r}/d^2t = m \vec{g} - a(mg \vec{v})/(\norm{\vec{v}}),

where a is the coefficient of aerodynamic friction.

The problem splits to the following:

1. (d v_x)/(d t) =  -a v_x/( \sqrt{(v^x)^2 + (v^y)^2} ) = func_v_x,
2. (d v_y)/(d t) = - g -a v_y/( \sqrt{(v^x)^2 + (v^y)^2} ) = func_v_y,
3. dx/dt = v_x = func_x,
4. dy/dt = v_y = func_y. '''


# Shot with Air Resistance with Linear Dependence from Velocity with a = 5
def func_x(t, x, y, v_x, v_y):
    return v_x

def func_v_x(t, x, y, v_x, v_y):
    a = 5
    return -a * (v_x/sqrt(v_x**2+v_y**2))

def func_y(t, x, y, v_x, v_y):
    return v_y

def func_v_y(t, x, y, v_x, v_y):
    g, a = 10, 5
    return -g - a * (v_y/sqrt(v_x**2+v_y**2))

# Runge Kutta 4^th Order
def shot_rk4(phi):
    # Time Step
    τ = 0.05

    t = np.zeros(200)
    y, v_y = np.zeros(200), np.zeros(200)
    x, v_x = np.zeros(200), np.zeros(200)

    # Errors
    e_x, e_y = np.zeros(200), np.zeros(200)

    # Initial Values
    t[0] = 0
    y[0], v_y[0] = 0, 20 * sin(phi)
    x[0], v_x[0] = 0, 20 * cos(phi)

    i = 0  # Counter
    while y[i] >= 0:
        # x - Direction
        k1x = τ * func_x(t[i], x[i], y[i], v_x[i], v_y[i])
        k1v_x = τ * func_v_x(t[i], x[i], y[i], v_x[i], v_y[i])
        k2x = τ * func_x(t[i] + t / 2, x[i] + k1x / 2, y[i], v_x[i] + k1v_x / 2, v_y[i])
        k2v_x = τ * func_v_x(t[i] + t / 2, x[i] + k1x / 2, y[i], v_x[i] + k1v_x / 2, v_y[i])
        k3x = τ * func_x(t[i] + t / 2, x[i] + k2x / 2, y[i], v_x[i] + k2v_x / 2, v_y[i])
        k3v_x = τ * func_v_x(t[i] + t / 2, x[i] + k2x / 2, y[i], v_x[i] + k2v_x / 2, v_y[i])
        k4x = τ * func_x(t[i] + t, x[i] + k3x, y[i], v_x[i] + k3v_x, v_y[i])
        k4v_x = τ * func_v_x(t[i] + t, x[i] + k3x, y[i], v_x[i] + k3v_x, v_y[i])
        x[i + 1] = x[i] + (k1x + 2 * k2x + 2 * k3x + k4x) / 6
        v_x[i + 1] = v_x[i] + (k1v_x + 2 * k2v_x + 2 * k3v_x + k4v_x) / 6
        # y - Direction
        k1y = τ * func_y(t[i], x[i], y[i], v_x[i], v_y[i])
        k1v_y = τ * func_v_y(t[i], x[i], y[i], v_x[i], v_y[i])
        k2y = τ * func_y(t[i] + t / 2, x[i], y[i] + k1y / 2, v_x[i], v_y[i] + k1v_y / 2)
        k2v_y = τ * func_v_y(t[i] + t / 2, x[i], y[i] + k1y / 2, v_x[i], v_y[i] + k1v_y / 2)
        k3y = τ * func_y(t[i] + t / 2, x[i], y[i] + k2y / 2, v_x[i], v_y[i] + k2v_y / 2)
        k3v_y = τ * func_v_y(t[i] + t / 2, x[i], y[i] + k2y / 2, v_x[i], v_y[i] + k2v_y / 2)
        k4y = τ * func_y(t[i] + t, x[i], y[i] + k3y, v_x[i], v_y[i] + k3v_y)
        k4v_y = τ * func_v_y(t[i] + t, x[i], y[i] + k3y, v_x[i], v_y[i] + k3v_y)
        y[i + 1] = y[i] + (k1y + 2 * k2y + 2 * k3y + k4y) / 6
        v_y[i + 1] = v_y[i] + (k1v_y + 2 * k2v_y + 2 * k3v_y + k4v_y) / 6
        # Time
        t[i + 1] = t[i] + τ
        # Counter
        i += 1

    # We Keep the Values for x and y != 0, respectively
    y, x = y[:i], x[:i]
    t = t[:i]

    return x[-1]

if __name__ == '__main__':

    phi = np.linspace(0, pi/2, 200)

    x_phi = np.zeros(200)

    i = 0
    for theta in phi:
        x_phi[i] = shot_rk4(theta)
        i += 1

    fig, ax = plt.subplots(1,1)

    fig.suptitle("Maximum Distance of Projectile Motion With Air Resistance")

    ax.plot(phi, x_phi, color='black', linewidth=1)
    # How Graph is Shown (axis titles)
    ax.set_ylabel(r'$x_{max}(\phi)$ $[\mathrm{m}]$')
    ax.set_xlabel(r'$\phi$ $[\mathrm{rad}]$')
    # Show the major grid lines
    ax.grid(b=True, which='major', color='#666666', linestyle='--')
    # Show the minor grid lines
    ax.minorticks_on()
    ax.grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.1)

    # Fix Quality
    fig.tight_layout()
    # Save the Graph
    fig.savefig('Maximum-Range.pdf')
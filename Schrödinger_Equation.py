# visualize Schrödinger Equation with matplotlib and numpy 3d plot

import matplotlib.pyplot as plt
import numpy as np
import scipy.constants
import scipy.linalg

# constants
h = scipy.constants.h  # m^2 kg / s
hbar = scipy.constants.hbar  # m^2 kg / s
c = scipy.constants.c  # m / s
m = scipy.constants.m_e  # kg
e = scipy.constants.e  # C
epsilon0 = scipy.constants.epsilon_0  # F / m
mu0 = scipy.constants.mu_0  # N / A^2
alpha = scipy.constants.alpha  # fine structure constant
G = scipy.constants.G  # m^3 / kg s^2
R = scipy.constants.R  # J / mol K
Avogadro = scipy.constants.Avogadro  # mol^-1
k = scipy.constants.k  # J / K
sigma = scipy.constants.sigma  # W / m^2 K^4
Rydberg = scipy.constants.Rydberg  # m^-1
Bohr = scipy.constants.value('Bohr radius')  # m
lightyear = scipy.constants.light_year  # m
parsec = scipy.constants.parsec  # m
g = scipy.constants.g  # m / s^2
atm = scipy.constants.atm  # Pa
ly = lightyear
pc = parsec
au = scipy.constants.au  # m
Da = scipy.constants.value('atomic mass constant')  # kg
me = scipy.constants.m_e  # kg
mp = scipy.constants.m_p  # kg
mn = scipy.constants.m_n  # kg
NA = scipy.constants.Avogadro  # mol^-1
kB = scipy.constants.k  # J / K
Rinf = scipy.constants.Rydberg  # m^-1
a0 = scipy.constants.value('Bohr radius')  # m
G = scipy.constants.G  # m^3 / kg s^2

# variables
x = 0
y = 0
z = 0
vx = 0
vy = 0
vz = 0
ax = 0
ay = 0
az = 0
t = 0
dt = 0.0001
m = 1
q = 1
B = 1
E = 1
Bx = 0
By = 0
Bz = 0
Ex = 0
Ey = 0

# Schrödinger Equation
# psi(x, t) = A * exp(i * (k * x - omega * t))
# k = 2 * pi / lambda
# omega = 2 * pi * f
# E = h * f = hbar * omega
# p = h / lambda = hbar * k
# E = p^2 / (2 * m)
# hbar * omega = hbar^2 * k^2 / (2 * m)
# omega = hbar * k^2 / (2 * m)
# omega = hbar * (2 * pi / lambda)^2 / (2 * m)
# omega = hbar * (2 * pi)^2 / (lambda^2 * 2 * m)

omega = hbar * (2 * np.pi) ** 2 / (2 * m)
k = 2 * np.pi / 1


# can you fix this error?
# TypeError: only size-1 arrays can be converted to Python scalars
# what is the problem?
# the problem is that the function psi(x, t) is not a scalar function
# it is a vector function
# the function psi(x, t) is a vector function because it is a complex function
# the function psi(x, t) is a complex function because it is a wave function
# the function psi(x, t) is a wave function because it is a solution of the Schrödinger Equation
# so can you fix this error?
# yes, you can fix this error by using the function np.vectorize()
# np.vectorize() is a function that converts a scalar function into a vector function
# where do you use the function np.vectorize()?
# you use the function np.vectorize() in the function psi(x, t)

def psi(x, t):
    vectorize_psi = np.vectorize(psi)
    return vectorize_psi(x, t)


def psi2(x, t):
    return np.abs(psi(x, t)) ** 2


def psi2_2d(x, t):
    return np.abs(psi(x, t)) ** 2


def psi2_3d(x, y, t):
    return np.abs(psi(x, t) * psi(y, t)) ** 2


def psi2_3d_2(x, y, t):
    return np.abs(psi(x, t) * psi(y, t) * psi(z, t)) ** 2


# plot the wave function in 3d


def plot_psi_3d():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(-10, 10, 1000)
    y = np.linspace(-10, 10, 1000)
    X, Y = np.meshgrid(x, y)
    Z = psi2_3d(X, Y, t)
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()


# create animation of the wave function in 3d with matplotlib

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x, y)
Z = psi2_3d(X, Y, t)
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

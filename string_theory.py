# code string theory

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


# functions
def f(x):
    return x


# code
print(f(1))
print(scipy.constants.value('Bohr radius'))
print(Bohr)
print(a0)
print(Bohr == a0)
print(Bohr == scipy.constants.value('Bohr radius'))
print(Bohr == scipy.constants.value('Bohr radius') == a0)
print(Bohr == scipy.constants.value('Bohr radius') == a0 == 5.2917721067e-11)
print(Bohr == scipy.constants.value('Bohr radius') == a0 == 5.2917721067e-11 == 5.2917721067e-11)
print(Bohr == scipy.constants.value('Bohr radius') == a0 == 5.2917721067e-11 == 5.2917721067e-11 == 5.2917721067e-11)
print(Bohr == scipy.constants.value(
    'Bohr radius') == a0 == 5.2917721067e-11 == 5.2917721067e-11 == 5.2917721067e-11 == 5.2917721067e-11)
print(Bohr == scipy.constants)

# plot f(x) with x from 0 to 100 using 2d plot
x = np.linspace(0, 100, 1000)
y = f(x)
plt.plot(x, y)
plt.show()

# use baesian statistics to predict where a particle will be in a quantum field after a certain amount of time and space and plot it in 3D

import math

import matplotlib.pyplot as plt
import numpy as np

# constants
h = 6.62607004e-34  # m^2 kg / s
hbar = h / (2 * math.pi)  # m^2 kg / s
c = 299792458  # m / s
m = 9.10938356e-31  # kg
e = 1.60217662e-19  # C
epsilon0 = 8.854187817e-12  # F / m
mu0 = 1.2566370614e-6  # N / A^2
alpha = 7.2973525664e-3  # fine structure constant
G = 6.67408e-11  # m^3 / kg s^2
R = 8.3144598  # J / mol K
Avogadro = 6.022140857e23  # mol^-1
k = 1.38064852e-23  # J / K
sigma = 5.670367e-8  # W / m^2 K^4
Rydberg = 10973731.568160  # m^-1
Bohr = 5.2917721067e-11  # m
lightyear = 9.4607304725808e15  # m
parsec = 3.0856775814914e16  # m
g = 9.80665  # m / s^2
atm = 101325  # Pa
ly = lightyear
pc = parsec
au = 149597870700  # m
Da = 1.660539040e-27  # kg
me = 9.10938356e-31  # kg
mp = 1.672621898e-27  # kg
mn = 1.674927471e-27  # kg
NA = Avogadro
kB = k
Rinf = Rydberg
a0 = Bohr
G = 6.67408e-11  # m^3 / kg s^2

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
Ez = 0
B = np.array([Bx, By, Bz])
E = np.array([Ex, Ey, Ez])
r = np.array([x, y, z])
v = np.array([vx, vy, vz])
a = np.array([ax, ay, az])


# functions
def lorentz_force(q, v, B, E):
    return q * (E + np.cross(v, B))


def acceleration(q, m, v, B, E):
    return lorentz_force(q, v, B, E) / m


def velocity(v, a, dt):
    return v + a * dt


def position(r, v, dt):
    return r + v * dt


def update(q, m, r, v, a, B, E, dt):
    a = acceleration(q, m, v, B, E)
    v = velocity(v, a, dt)
    r = position(r, v, dt)
    return r, v, a


def main():
    r = np.array([x, y, z])
    v = np.array([vx, vy, vz])
    a = np.array([ax, ay, az])
    B = np.array([Bx, By, Bz])
    E = np.array([Ex, Ey, Ez])
    t = 0
    while t < 10:
        r, v, a = update(q, m, r, v, a, B, E, dt)
        t += dt
        print(r, v, a)


main()

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(r[0], r[1], r[2], c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()

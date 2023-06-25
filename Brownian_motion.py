# code the equation brownian motion using the random module and plot it using weierstrass function in 3d

import math
import random

import matplotlib.pyplot as plt
# import modules
import numpy as np

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
    for i in range(1000):
        r, v, a = update(q, m, r, v, a, B, E, dt)
        plt.plot(r[0], r[1], 'o')
    plt.show()


main()


# code the equation brownian motion using the random module and plot it using weierstrass function in 3d

def brownian_motion(x, y, z, t, dt):
    for i in range(1000):
        x += random.uniform(-1, 1) * math.sqrt(dt)
        y += random.uniform(-1, 1) * math.sqrt(dt)
        z += random.uniform(-1, 1) * math.sqrt(dt)
        plt.plot(x, y, z, 'o')
    plt.show()


brownian_motion(x, y, z, t, dt)


# make a simulation of a particle in a box using the random module and plot it using weierstrass function in 3d

# make this 3d
def particle_in_a_box(x, y, z, t, dt):
    for i in range(1000):
        x += random.uniform(-1, 1) * math.sqrt(dt)
        y += random.uniform(-1, 1) * math.sqrt(dt)
        z += random.uniform(-1, 1) * math.sqrt(dt)
        t += dt
        plt.plot(x, y, z, 'o')
    plt.show()


particle_in_a_box(x, y, z, t, dt)

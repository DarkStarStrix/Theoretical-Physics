# Code the equation of special relativity using the random module and plot it using weierstrass function in 3d

import matplotlib.pyplot as plt
# In[ ]:
import numpy as np
import random

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


def main(t=1):
    global r, v, a
    for i in range(int(t / dt)):
        r, v, a = update(q, m, r, v, a, B, E, dt)
        print(r, v, a)
        # plt.plot(r[0], r[1], 'ko')
        # plt.show()
        # plt.pause(0.0001)
        # plt.clf()
    return r, v, a


main(1)

# # calculate the lorentz force using the random module and plot it using weierstrass function in 3d
# lorentz_force(q, v, B, E)
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(lorentz_force(q, v, B, E)[0], lorentz_force(q, v, B, E)[1], lorentz_force(q, v, B, E)[2], c='r', marker='o')
# plt.show()
#
# # plot the weierstrass function in 3d
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(lorentz_force(q, v, B, E)[0], lorentz_force(q, v, B, E)[1], lorentz_force(q, v, B, E)[2], c='r', marker='o')
# plt.show()

# plot the lorentz force using the random module and plot it using weierstrass function in 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(lorentz_force(q, v, B, E)[0], lorentz_force(q, v, B, E)[1], lorentz_force(q, v, B, E)[2], c='r', marker='o')
plt.show()


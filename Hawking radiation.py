# code the hawking radiation formula calculate how long it takes for a black hole to evaporate based on its mass

# In[ ]:

import scipy.constants
import math
import matplotlib.pyplot as plt
import numpy as np

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

# In[ ]:

# code the hawking radiation formula calculate how long it takes for a black hole to evaporate based on its mass
#  of black hole
# M = 1
# # mass of electron
# m = scipy.constants.m_e
# # mass of proton
# mp = scipy.constants.m_p
# # mass of neutron
# mn = scipy.constants.m_n

# # calculate the lifetime of the black hole
# t = (5120 * math.pi * G**2 * M**3) / (hbar * c**4 * (m + mp + mn)**2)
# print(t)

# calculate the lifetime of the black hole in years and plot it against the mass of the black hole in kg on a 3d graph
#  of black hole
M = 100000
# mass of electron
m = scipy.constants.m_e
# mass of proton
mp = scipy.constants.m_p
# mass of neutron
mn = scipy.constants.m_n

# calculate the lifetime of the black hole
t = (5120 * math.pi * G ** 2 * M ** 3) / (hbar * c ** 4 * (m + mp + mn) ** 2)
print(t)

line = np.linspace(0, 100, 100)  # 100 evenly spaced numbers between 0 and 100
x, y = np.meshgrid(line, line)  # create a grid of points
z = (5120 * math.pi * G ** 2 * x ** 3) / (
        hbar * c ** 4 * (m + mp + mn) ** 2)  # calculate the z values for each point of the grid
fig = plt.figure()  # create a figure
ax = fig.add_subplot(111, projection='3d')  # create a 3d subplot
ax.plot_surface(x, y, z)  # plot the surface
ax.set_xlabel('Mass of black hole (kg)')  # label the x-axis
ax.set_ylabel('Time (years)')  # label the y axis
ax.set_zlabel('Mass of black hole (kg)')  # label the z axis
plt.show()  # show the plot


# make a new module that calculates the lifetime of a black hole based on its mass
def hawking_radiation(M):
    # mass of electron
    m = scipy.constants.m_e
    # mass of proton
    mp = scipy.constants.m_p
    # mass of neutron
    mn = scipy.constants.m_n

    # calculate the lifetime of the black hole
    t = (5120 * math.pi * G ** 2 * M ** 3) / (hbar * c ** 4 * (m + mp + mn) ** 2)
    return t

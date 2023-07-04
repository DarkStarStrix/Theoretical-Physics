# code the Schwarzschild  radius

import matplotlib.pyplot as plt
# import packages
import numpy as np

# calculate the Schwarzschild radius of the sun in meters
G = 6.67408e-11  # m^3 kg^-1 s^-2
c = 2.99792458e8  # m s^-1
M_sun = 1.989e30  # kg
# change the units of the Schwarzschild radius to meters by multiplying by 2 and making the units int
R_s = 2 * G * M_sun / c ** 2
print(R_s)


# plot the Schwarzschild radius of the sun in meters in 3d
# define the function
def f(x, y):
    return x ** 2 + y ** 2


# define the grid
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)

# calculate the function value
Z = f(X, Y)

# plot the function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Schwarzschild Radius of the Sun in Meters')
ax.view_init(30, 30)
ax.set_zlim(0, 1)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zticks([0, 0.5, 1])
ax.set_xticks([-1, -0.5, 0, 0.5, 1])
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
plt.show()




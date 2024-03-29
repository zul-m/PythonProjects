import numpy as np
import matplotlib.colors as col
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
x, y = np.meshgrid(x, y)

z = f(x, y)

# Wireframes plots.
fig = plt.figure()

ax = plt.axes(projection = '3d')
ax.plot_wireframe(x, y, z, color = 'black')
ax.set_title('wireframe')

plt.show()

# Surface plots.
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, rstride=1,
                cstride=1, cmap='viridis',
                edgecolor='none')
ax.set_title('surface')

plt.show()
# Plot a fraph of a function

import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D  # Import necessary for 3D plotting

# -----------------------
#      Plot 2D Graph 
# -----------------------

# def f(x):
#     return x**2

# xList = np.arange(-10, 10, 0.1)

# yList = f(xList)

# plt.figure(num=0, dpi=120)
# plt.plot(xList, yList)
# plt.show()


# -----------------------
#      Plot 3D Graph 
# -----------------------

# Define the function
def f(x, y):
    return x**2 + y**2

# Create a grid of x and y values
x = np.linspace(-10, 10, 100)  # X-axis range
y = np.linspace(-10, 10, 100)  # Y-axis range
X, Y = np.meshgrid(x, y)       # Create a 2D grid
Z = f(X, Y)                    # Calculate Z values for the grid

# Create the 3D plot
fig = plt.figure(dpi=120)
ax = fig.add_subplot(111, projection='3d')  # 3D subplot
surf = ax.plot_surface(X, Y, Z, cmap='viridis')  # Surface plot with a colormap

# Add labels and a color bar
ax.set_title("3D Plot of f(x, y) = x^2 + y^2")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis (f(x, y))")
fig.colorbar(surf, shrink=0.5, aspect=10)  # Color bar for reference

# Show the plot
plt.show()
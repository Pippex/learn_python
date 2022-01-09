import random as rd
import matplotlib.pyplot as plt
import pandas as pd

ax = plt.axes(projection="3d")


x_cord = 0
y_cord = 0
z_cord = 0
x_walk = []
y_walk = []
z_walk = []
negative_positive = [-1, 1]

for i in range(10000):
    x_walk.append(x_cord)
    y_walk.append(y_cord)
    z_walk.append(z_cord)
    x_cord += 0.1*negative_positive[rd.randint(0,1)]
    y_cord += 0.1*negative_positive[rd.randint(0,1)]
    z_cord += 0.1*negative_positive[rd.randint(0,1)]

x_walk.append(x_cord)
y_walk.append(y_cord)
z_walk.append(z_cord)


total_walk = pd.DataFrame(x_walk, y_walk)
total_walk[2] = z_walk
print(total_walk.head())
plt.title("This is the Hermes Walk")
ax.plot3D(x_walk, y_walk, z_walk)
plt.show()
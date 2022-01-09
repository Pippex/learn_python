import random as rd
import matplotlib.pyplot as plt
import pandas as pd


x_cord = 0
y_cord = 0
x_walk = []
y_walk = []
negative_positive = [-1, 1]

for i in range(1000000):
    x_walk.append(x_cord)
    y_walk.append(y_cord)
    x_cord += 0.1*negative_positive[rd.randint(0,1)]
    y_cord += 0.1*negative_positive[rd.randint(0,1)]

total_walk = pd.DataFrame(x_walk, y_walk)
print(total_walk.head())
plt.plot(total_walk)
plt.show()
import random as rd
import matplotlib.pyplot as plt

generated_numbers = []

def how_many_items(iterator, item):
    counter = 0
    for i in iterator:
        if i == item:
            counter += 1

    return counter

for i in range(1000000):
    generated_numbers.append(rd.randint(1,100))
    
plt.hist(generated_numbers, 100)
plt.show()


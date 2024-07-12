#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt
#name = input("Enter name: ")


x = [i for i in range(25)]
x = np.array(x)

y = x**2

plt.plot(x,y)
plt.savefig("plot_example.png")

#print("Hello " + name)


#Simple comment

#Another comment

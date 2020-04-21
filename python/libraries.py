print("printing 2D array using numpy module")

import numpy as nm
import matplotlib.pyplot as mtp
x = [[2,3,4],[5,6,7],[8,9,10]]
a = nm.array(x)
print(a)

print("printing graph type representation using matplotlib module")


'exec(%matplotlib inline)'
x = nm.linspace(0,10,100)
y = x ** 2
mtp.plot(x,y)

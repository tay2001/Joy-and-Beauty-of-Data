##taylor powell
##checkerboard

##-------------------------------

##import numpy
import numpy as np


##first array with ones and zeros??
x = np.ones((3,3))

##print(x)

x = np.zeros((8,8),dtype=int)

x[1::2,::2] = 1
x[::2,1::2] = 1

print(x)

print('\n')


##--------------------------------
##2nd with 3 and 0

y = np.zeros((8,8),dtype=int)

y[1::2,::2] = 3
y[::2,1::2] = 3

print(y)

print('\n')

##--------------------------------
##2nd with 4 and 7
z = np.full(64,4).reshape(8,8)

z[1::2,::2] = 7
z[::2,1::2] = 7

print(z)



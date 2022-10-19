##taylor powell
##arrays
##--------------------

##import numpy
import numpy as np

##make v
v = np.random.randint(1,100,size=(10))

print(v)
print('\n v1 with odd indices of v')

##make v1 - with the odd indices from v
v1 = v[1::2]

print(v1)
print('\n v2 w/ backwards ordering')

##make v2 - with the backwards ordering from v
v2 = v[::-1]

print(v2)
print('\n make m')

##make m - with 25 evenly sep # from 6 to 21 in 5x5
m = np.linspace(6,21,25).reshape(5,5)
print(m)
print('\n reverse cols of m')

##reverse the columns of m
m1 = m[::,::-1]
print(m1)
print('\n reverse rows of m')

##reverse the rows of m
m2 = m[::-1,::]
print(m2)
print('\n reverse both of m')

##reverse both of m
m3 = m[::-1,::-1]
print(m3)
print('\n turn rows into cols')

##make rows = columns, different then last one
m4 = m.transpose(1,0)
print(m4)
print('\n Cut off first and last row + col')

##cut off the first and last row + column
m5 = m[1:-1,1:-1]
print(m5)
print('\n 3D')

##make 3d array
p= np.arange(1, 65).reshape(4,4,4).transpose(2,0,1)
print(p)
print('\n only second layer')

##make only second layer
    ##not really sure if this is right?
print(p[1,:])
print('\n')






##taylor powell
##histogram

##-----------------

#import
import numpy as np
import matplotlib.pyplot as plt

##get some values for an equation for x
a=100
b= 50
x = a + b*np.random.randn(251)

# the histogram of the data
n, bins,patches= plt.hist(x, 50, density=1, facecolor='green',align='left')

##label the axis
plt.xlabel('x axis')
plt.ylabel('yaxis')

##give it a title
plt.title('Histogram')

##set the axis
plt.axis([40, 160, 0, 0.03])

##give it a grid
plt.grid(True)

##show it
plt.show()


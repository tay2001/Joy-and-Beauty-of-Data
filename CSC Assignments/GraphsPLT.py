import numpy as np
import matplotlib.pyplot as plt

##x = [1,2,3,4,5]
##y = [.5,5,6,8,1]

x=[17,17,18,18,18,18,19,19,19,20,20,25,27]
plt.hist(x,10,facecolor='green',density=1)

plt.xticks([16,17,18,19,20,21,22,23,24,25,26,27,28])


##x = np.linspace(0,25)
##y = (x**4)+(2*(x**3))+(x**2)-3
##z = 500*x**2-20
##
##
##plt.title('cool chart', fontsize = 18, color = 'green')
##plt.xlabel('x', fontsize = 18, color = 'green')
##plt.ylabel('y',fontsize = 18, color = 'green')
##plt.text(10,300000, 'y=x**4+2*x*x**3+x**2-3')
##
##plt.xlim(-10,40)
##plt.axis([-10,40,-100000,500000])
##
##plt.grid(1)
##
##plt.figure(1)
##plt.subplot(212)
##plt.plot(x,y,'red',x,z,'blue',linewidth=3)
##
##plt.subplot(211)
##plt.plot(x,z,'blue',linewidth=2)

plt.show()

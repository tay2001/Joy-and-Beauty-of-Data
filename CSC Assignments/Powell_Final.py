##taylor powell
##final
##----------------------------##

##all imports
import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

##---------------------------------
##equation y=.5*x-2
##x=-5 y and 0 is <.01

#error
error = 1

##equation
x=-5
y=.5*x-2

real = y

prevy = y

while error >= .01:
    y = (y + x/y)/2-2
    error = abs(y - prevy)
    prev_y = y
    x=x+.1

print('here is x ' , x , 'here is error ', error,)


####----------------------------------##

##lists
fish = ['salmon','trout','bass','bluegill','perch','crappie','bullhead']
size = [6,4,7,3,2,3,9]
quantity = [18,24,13,32,44,3,9]

##zip n make dataframe
fsq = list(zip(fish,size,quantity))
fishes = pd.DataFrame(data=fsq,columns=['fish','size','quantity'])

##create file
fishes.to_csv('fish.csv',index=False,header=True)

##print fishes
print(fishes)

##create graph
graph_title = "Fish Study"
x_axis = fishes.columns[0]
y_axis = fishes.columns[1:]

fishes.plot(title=graph_title, x=x_axis, y=y_axis, kind='bar', color=['blue','green'], legend = True)

plt.show()


##--------------------------------##

##make 3d array 100 inclusive
scores = np.random.randint(0,101,size=(10,5,4))


##set up the plot
sp1=scores[:,1,1]
sp2 = scores[:,1,3]
plt.xticks = [0,2,4,6,8]
plt.yticks = [0,20,40,60,80]
plt.title('Spring Semesters', fontsize = 18, color = 'blue')
plt.xlabel('Student ID', fontsize = 18, color = 'blue')
plt.ylabel('Course 2 Scores', fontsize = 18, color = 'blue')

##plot it
plt.plot(sp1,'b--',linewidth=2)
plt.plot(sp2,'green',linewidth=2)
plt.show()

##find average
avgscores= []
i = 0

for avg in scores:
    avg = scores[i].mean()
    avgscores.append(avg)
    i+=1
    

##find highest one
av1=max(avgscores)
print('Student ID: ',avgscores.index(av1))
print('Highest grade avg: ',av1)
print("Complete Record = \n" , scores[avgscores.index(av1)])

##----------------------------------------

class Pyth:
    """ """
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def add(self):
        add = self.a**2 + self.b**2
        return ' c= ' + str(add)

    def __str__(self):
        return ('a= ' + str(self.a) + ' b= ' + str(self.b))

    
prob_1 = Pyth(5, 12)

print(prob_1 , prob_1.add())



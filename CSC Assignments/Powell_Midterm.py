##programmer: taylor powell
##Midterm

##import turtle, math, etc beforehand
import turtle
import math
import string
import random

##problem 1 - golden ratio
##
##x = 4
##
##equa_x = 1 + 1/x
##
##error = 1
##
##ask = float(input("What decimal (.001 or something similar) would you like it to round too?"))
##
##real = equa_x
##
##prev_equa_x = equa_x
##while error > ask:
##    equa_x = (equa_x + x/equa_x)/x
##    error = abs(equa_x-prev_equa_x)
##    prev_equa_x = equa_x
##
##print("true value(from loop)=",equa_x)
##print("actual value=",real)




##problem 2 - turtle graphics
##set up turtle
##win = turtle.Screen()
##
##t = turtle.Turtle()
##t.shape('turtle')
##
####first color size etc
##color_list = ['blue','red','green']
##sides = 8
##size = random.randint(1,5)
##
####speed up the drawing
##t.speed(8)
##
##t.setheading(0)
##    
####get the colors goin'
##t.color(random.choice(color_list))
##
##t.fillcolor(random.choice(color_list))
##t.begin_fill()
##
####rectangle
##for i in range(sides):
##    t.forward(15* size)
##    t.left(random.randint(1,180))
##
##t.end_fill()



             
##problem 3 - reverse alphabetical

####names list
##names = ['Max', 'Sam', 'Cameron', 'Karl', 'Taylor', 'Ethan', 'Bryce']
##
####sort them first
##list.sort(names)
####then reverse
##list.reverse(names)
####print
##print(names)





##problem 4 - slicing

##alphabet = ["a","b","c","d","e","f","g","h",'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
##
##a = alphabet[-3:]
##b =alphabet[0:5]
##c = alphabet[9:12]
##
##
##newstring = a+b+c
##print(newstring)





####problem 5 - total snowfall before 2000
####big list
##snowfall = [[1992, 115],[2001,98],[2003, 84],[1995,96],[1999,55],[2019,120],[2012,65]]
##
####splice into two
##years = [i[0] for i in snowfall]
##fall = [i[1] for i in snowfall]
##
####function to get total snowfall from years b4 2000
##def check_snowfall():
##    ##set variables
##    i = 0
##    total = 0
##    
##    ##loop to check
##    for i in range(len(snowfall)):
##        ##if statement to check if years are less than 2000
##        if years[i] > 2000:
##            i+=1
##        ## else add it to the total
##        else:
##            total = total + fall[i]
##            i += 1
##    ##return the total
##    return total
##
####main function + print
##def main():
##    ##call snowfall make total equal to it
##    total = check_snowfall()
##
##    ##print the total
##    print("total snowfall in years before 2000 =" , total)
##
####call main :)
##main()
        








        
        


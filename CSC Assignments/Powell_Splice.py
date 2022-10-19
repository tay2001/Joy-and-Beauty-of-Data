##programmer: taylor powell
##assignment: splice

##import string
import string

##variables

x = "NICK"

y = "DE JAVU"

z = "Bob!"

##start slicing

##slice the first variable

a = x[0:3]

##slice the next one

b = y[1:4]

##slice the final one

c = z[-3:]

##force appropriate capitalization
##combine for the 'nice'
d = a+b
d = d.replace("ICE","ice")


##combine them together finally
f = d + c

##center it
f = f.center(40)

##print it
print(f)


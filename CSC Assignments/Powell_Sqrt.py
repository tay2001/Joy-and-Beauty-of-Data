##programmer: taylor powell
##assignment: square root

##import math just in case
import math

##variables
error = 1

##get the user supplied number
n = float(input("Please give a number to get the square root of: "))

##initial equation//guess
sn = .5*n

##print the initial guess
print("The initial guess is:" ,sn)

##prev sn
prev_sn = sn
    
##make the while loop w/ error
while error > .01:
    ##equation
    sn=(sn + n/sn)/2
    ##error
    error = abs(sn - prev_sn)
    ##prev sn
    prev_sn = sn

##Print the while loops answer
print("True value: ",sn)

##actual value using math library
print("Actual value: ", math.sqrt(n))


##:)

    
    



##programmer: taylor powell
##assignment: Guess Game

##import random
import random

##variable for random num
rnum = random.randint(0,11)

##set up the counter
c = 0

##get the input
guess = int(input("Enter an integer from 1 to 10: "))

##make a while loop
while rnum != "guess":
    ##if guess is too low
    if guess < rnum:
        print("Guess is low!")
        guess = int(input("Enter an integer from 1 to 10: "))
        c += 1
    ##if guess is too high
    elif guess > rnum:
        print("Guess is high!")
        guess = int(input("Enter an integer from 1 to 10: "))
        c += 1
    ##if you guess it
    else:
        print("You got it! The number was " ,rnum, ". Your total number of guesses was ",c,".")
        break

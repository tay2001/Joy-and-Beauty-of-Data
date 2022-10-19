##programmer: taylor powell
##assignment: uno

## lets get random in on this
import random

##make a list
color_list = ["red","yellow","green","blue"]

##set variables

f_color = random.choice(color_list)

f_value = random.randint(1,10)

s_color = random.choice(color_list)

s_value = random.randint(1,10)

##set boolean function

def legal_play(f_value, f_color, s_value, s_color):
    ##if the colors match or nums math or both
    if f_value == s_value or f_color == s_color:
        print("True")
        return True
    else:
        print("False")
        return False

##call the function

legal_play(f_value, f_color, s_value, s_color)

legal_play(3, "blue", 3, "green")
legal_play(5, "yellow", 7, "yellow")
legal_play(9, "red", 6, "green")



    

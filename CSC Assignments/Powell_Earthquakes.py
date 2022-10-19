##programmer: taylor powell
##assignment: earthquake file

# The missing functions go here.

##avg magnitude, w file as an arg)
def average_magnitude(file):
    ##open the file
    eq_file = open(file,"r")

    ##i believe to skip the first line aka labels
    next(eq_file)

    ##counter for how many magnitude values
    i = 0

    ##placeholder for the total magnitude
    t_mag = 0.0

    ##for loop to get the values
    for line in eq_file:
        ##split the lists at the ','
        mags = line.split(",")
        ##use negative index to accurately get the numbers, float it
        t_mag += float(mags[-8])
        ##add one to the counter - rinse n repeat
        i += 1

    ##close the file
    eq_file.close()

    ##return the average mag w/ the math
    return t_mag / i
        

##count the amt of earthquakes that exceed the user bounds
def count_earthquakes(file, low, up):
    ##open file again
    eq_file = open(file,"r")
    ##skip the first line again
    next(eq_file)
    ##counter for how many again
    i = 0

        ##loop to get the amt
    for line in eq_file:
        mags = line.split(",")
        ##use the negative index again
        all_mags = float(mags[-8])
        ##if statement to see if it meets the conditionals provided by User
        if low <= all_mags <= up:
            i += 1

    ##close
    eq_file.close()

    ##return the value
    return i


##function for locations
def earthquake_locations(file):
    ##open it once more
    eq_file = open(file,"r")
    ##skip first line oncemore
    next(eq_file)
    ##list for locos
    locos = []

    ##numbers counter
    num = 1

    ##get the print statement rdy
    print("Alphabetical Order of Earthquake Locations")
    ##cant forget that line tho :]
    print("------------------------------------------")
    
    ##for loop almost same as b4
    for line in eq_file:
        ##same as b4
        places = line.split(",")
        ##go the right - index for loco
        loco = places[-5]

        ##if loco not in locos
        if loco not in locos:
            locos += [loco]

    ##sort em
    locos.sort()
    
    ##another for loop
    for loco in locos:
        print(str(num) + "." + loco)
        num += 1

    print()
    eq_file.close()



def main(file):
    magnitude = average_magnitude(file)
    print("The average earthquake magnitude is {:.2f}\n".format(magnitude))
    
    earthquake_locations(file)
    
    low = float(input("Enter a lower bound for the magnitude: "))
    up = float(input("Enter an upper bound for the magnitude: "))
    i = count_earthquakes(file, low, up)
    print("Number of recorded earthquakes between {:.2f} and {:.2f} = {:d}".format(low, up, i))



main("earthquakes")



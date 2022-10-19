##programmer: taylor powell
##assignment: rain list

##import string just in case
import string

##big combined list - used for the for loop at the bottom
rainfall = [["2001",18.2],["03",21.5],["04",1.74],["05",20.2],["06",203],
            ["2007",23.1],["10",1.93],["13",18.7],["16",176],["17",16.5],
            ["2019",18.8]]

##splice into two sep lists
year_list = [i[0] for i in rainfall] 
rainfall_num = [i[1] for i in rainfall]

##make rainfall_num a string list
rainfall_num = [str(x) for x in rainfall_num]

##variable for old + string > list
rf_num2 = [i[1] for i in rainfall]
rf_num2 = [str(x) for x in rainfall_num]

print(type(rf_num2))


##check the years to see if they are right
def check_year():
    ##for i is still in the index
    for i in range(len(year_list)):
        ##check if the element length is four
        if len(year_list[i]) == 4:
            i += 1
        ##else add "20"
        else:
            year_list[i] = "20" + year_list[i]
            i += 1
            

####check the decimals and fix
def check_rainfall():

    ##set variables
    i=0
    i_string = ''
    d = '.'


    
    ##for loop for i in range of the length
    for i in range(len(rainfall_num)):
        if d in rainfall_num[i]:
            
            ##make it a string w/o decimal point
            rainfall_num[i] = rainfall_num[i].replace(".","",1)
            i_string = rainfall_num[i]
            
            ##add decimal in right spot
            i_string = i_string[:2] + d + i_string[2:]
            
            ##check if it is the same as orig, if not, print c
            if rf_num2[i] == i_string:
                i_string = i_string
                
            else:
                i_string = i_string + "\t\tc"
                
            ##make it = i_string again
            rainfall_num[i] = i_string

            ##next term
            i += 1
                
        ##if it didn't have a decimal
        else:
            ##make a new string
            i_string = rainfall_num[i]

            ##add decimal to new string
            i_string = i_string[:2] + d + i_string[2:]

            ##check if it is the same as orig, if not, print c
            if rf_num2[i] == i_string:
                i_string = i_string
            else:
                i_string = i_string + "\t\tc"
                
            ##make the element = the string
            rainfall_num[i] = i_string
            
            ##next term
            i += 1


    


##funct for finding and correcting year
def display():
    ##for loop to display it
    for i in range(len(rainfall)):
            print(year_list[i],"\t",rainfall_num[i]) 
        
        
##main function

def main():
    ##print the 'Year' and 'rain'
    print("Year \t Rainfall (in)")

    ##print all our functions
    check_rainfall()
    check_year()    
    display()

##call main!
main()


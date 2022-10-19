##programmer: taylor powell
##assignment: census


##import math
import math


##top 10 most populous - nested-lists
populations = [["California", 38332521],
               ["Texas", 26448193],
               ["New York", 19651127],
               ["Florida", 19552860],
               ["Illinois", 12882135],
               ["Pennsylvania", 12773801],
               ["Ohio", 11570808],
               ["Georgia", 9992167],
               ["Michigan", 9895622],
               ["North Carolina", 9848060]]

total_US = 316128839


##get the total population - pure function!!
def total_pop(population):
    ##get the sum
    return sum(population)


##function to get % of who - wasn't sure if it needed to be pure but i did it
def total_percent(pop_total, total_US):
    ##return the percentage
    return pop_total/total_US

    



##main to call everything n print
def main():
    ##split the lists out one states one population
    population = [i[1] for i in populations]
    states = [i[0] for i in populations]

    ##make pop_total = to callin the returned value and print
    pop_total = total_pop(population)
    print("The total population in the top 10 is:" ,pop_total, "people.")

    ##print the percent, but times by 100
    percent_total = pop_total/total_US*100
    print("The total percent of the population living in the Top 10 is:" ,round((percent_total)),"%.")
    
    


main()

    




##programmer: taylor powell
##assignment: grades

##import
import string

##funct to get the scores
def getScores(file):
    ##open file
    file = open(file,'r')
    
    ##skip headers
    next(file)

    ## list to store
    gradeset1 = []

    ##counter
    i = 0

    ##loop thru to get first one
    for line in file:
        ##split em
        grades1 = line.split(",")
        ##negative index poss?
        all_grades1 = int(grades1[-2])
        ##put it in the lists
        gradeset1.append(all_grades1)
        ##go thru all lines
        i+=1


    ##closet it
    file.close()

    ##return it
    return gradeset1



##get second set of scores
def getScores2(file):
    ##open file
    file = open(file,'r')

    ##skip the first line
    next(file)

    
    ## list to store
    gradeset2 = []

    ##counter
    i = 0

    ##loop thru to get first one
    for line in file:
        ##split em
        grades2 = line.split(',')
        ##negative index poss?
        all_grades2 = int(grades2[-1])
        ##put it in the lists
        gradeset2.append(all_grades2)
        ##go thru all lines
        i+=1

    ##closet it
    file.close()

    ##return it
    return gradeset2



##funct to get the average from the lists
def getAverage(set1,set2):
    
    ##list for storage
    avglist = []

    ##counter
    i = 0

    ##loop to get em
    while 4 >= i:
        ##make scores variables
        s1 = set1[i]
        s2 = set2[i]
        ##add the scores
        avg = s1+s2
        ##divide
        avg = avg/2
        ##add it to list
        avglist.append(avg)
        ##counter to go thru
        i += 1
    
    return avglist

##make a new file grades2
def grades2(file, avglist):
    ##open file
    file = open(file,'r')
    grades2 = open('grades2.csv','w')

    ##convert float list to str
    avg = [str(i) for i in avglist]

    ##counter
    i = 0

    ##read the lnes
    file.readline()
    ##write the headers - I left the tabs out so they lined up better
    grades2.write("Name         Program1     Program2   Average \n")
    ##search the lines
    for line in file:
        ##split em
        score = line.split('\n')
        ##replace the \ns with \ts, then \ts ,s
        line = line.replace('\n','\t')
        line = line.replace(',','\t')
        ##add the averages in
        line = line + '\t' + (str(avg[i] + '\n'+'\t'))
        ##write em
        grades2.write(line)
        ##count up
        i += 1

     ##close em                      
    file.close()
    grades2.close()
    

def main(file):
    ##get sets
    set1 = getScores(file)
    set2 = getScores2(file)

    ##get averages
    avglist = getAverage(set1,set2)

    ##open new file
    grades2(file, avglist)

main("grades.csv")
    








##programmer: taylor powell
##ascii assignment


# The missing functions go here.

##create the dictionary function
def create_dictionary(file):

    ##create dictionary
    d = {}

    ##line in the file
    for line in open(file,'r'):
        #strip em
        line = line.strip()
        #split em into the columns
        fascii,letter= line.split(',')
        ##put them in
        d[letter] = fascii


##replace space and comma
    del d['space']
    del d['comma']

    d[' '] = '00100000'
    d[','] = '00101100'

    
    ##return the dicitionary
    return d
    


##translate function
def translate(sentence, dictionary, filename):
    ##open a output file!
    translated = open(filename,'a')

    ##placeholder string
    decodeString = ""

    ##Sentence
    x = sentence
    
    ##temp list to hold the sentence
    z =[sentence]

    ##for loop to split into individual character
    for item in z:
        for character in item:
            ##check if not in dict, if not add it as unknown
            if character not in dictionary:
                dictionary[character] = 'UNKNOWN'
                
##run while length of sentence aint 0
    while len(x) > 0:
        for currentSearch in dictionary:
            ##if currentsearch is in the sentence
            if currentSearch in x[:len(currentSearch)]:
                ##add the value to the decodeString
                    decodeString += dictionary[currentSearch]
                    ##make x = x with the current search
                    x = x[len(currentSearch):]
                    ##Write it into the file
                    translated.write(currentSearch + ' ' + dictionary[currentSearch] + '\n')


                
    ##close n ur done!
    translated.close()
    print(x)
    



# --------------------------------------

def main():
    dictionary = create_dictionary("ascii-code.csv")
    sentence = "Buck lived at a big house in the sun-kissed Santa Clara Valley. Judge Miller's place, it was called!"
    translate(sentence, dictionary, "output-1.txt")
    print('\n')
    sentence = "Bozeman, MT  59717"
    translate(sentence, dictionary, "output-2.txt")
    print('\n')
    sentence = "The value is ~$25.00"
    translate(sentence, dictionary, "output-3.txt")

##--------------------------------------

main()

create_dictionary("ascii-code.csv")

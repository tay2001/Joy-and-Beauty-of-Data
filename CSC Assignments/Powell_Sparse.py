import string

# --------------------------------

##make it to words
def sentence_to_words(sentence):
    ##make it all lowercase
    sentence = sentence.lower()
    ##new one to hold em
    rsentence = ""
    ##characters in the sentence
    for char in sentence:
        ##that are lowercase or spaces
        if char in string.ascii_lowercase or char == " ":
            ##add it each time
            rsentence += char
            ##return that boi
    return rsentence

# --------------------------------
##update the dictionaryyyyy
def update(dictionary, words):
    ##look for the word in the words
    for word in words:
        ##add it to em
        dictionary[word] = dictionary.get(word, 0) + 1

# --------------------------------

##find the most frequent used word
def most_frequent(dictionary):
    ##total of the dict values
    total = dictionary.values()
    ##max total
    max_total = max(total)
    ##print the total
    print("Number of times used: " , max_total)
    ##get the value amts
    for i, value in dictionary.items():
        if max_total == value:
            print("The word is:", i)

# --------------------------------

def main():
    proceed = "yes"
    word_dictionary = {}
    while proceed == "yes" or proceed == "y":
        sentence = input("Please enter a sentence: ")
        words = sentence_to_words(sentence)
        word_list = words.split()
        update(word_dictionary, word_list)
        print(word_dictionary)
        most_frequent(word_dictionary)
        proceed = input("Would you like to continue? ")
        proceed = proceed.lower()

# --------------------------------

main()

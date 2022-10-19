##programmer: taylor powell
##notes: dictionaries cont. 10/24

import string

# ---------------------------

def keep_letters(filename):
    file = open(filename, "r")
    modified_text = ""

    for line in file:
        line = line.lower()
        for letter in line:
            if letter in string.ascii_lowercase:
                modified_text += letter

    file.close()
    return modified_text

def count_letters(text):
    count = {}
    for letter in string.ascii_lowercase:
        count[letter]=0
    for letter in text:
        count[letter] = count[letter] + 1
    print(count)

# ---------------------------

text = keep_letters("raven.txt")

count_letters(text)
print(text)

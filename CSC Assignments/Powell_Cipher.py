##programmer: taylor powell
##assignment:caesar cipher

##import string lib
import string

##variables
string = ''
shift = 0
mult = 0

##define c for true or false
c = True

##possibly encrypt??
def encrypt(string,shift,mult):

    ##string
    cipher = ' '

    ##loop to get the letters
    for char in string:
        if char == " ":
            cipher = cipher + char

        ##check if the char is the * then replace
        elif char == "*":
            cipher = cipher + char.replace("*"," ")

        ##check if uppercase
        elif char.isupper():
            
            ##apply the shift
            cipher = cipher + chr(int((a*ord(char) + (shift))))

        ##else, apply the shift    
        else:
            ##apply the shift
            cipher = cipher + chr(int((a*ord(char) + (shift))))
        
    ##return the letters
    return cipher


##------------------------------------------------------##


##create function for decryption
def decrypt(string, shift,mult):
    ##string
    cipher = ' '

    ##loop to get the letters
    for char in string:
        
        ##check if the char is space then save
        if char == " ":
            cipher = cipher + char

        ##check if the char is the * then replace
        elif char == "*":
            cipher = cipher + char.replace("*"," ")

        ##check if uppercase
        elif char.isupper():
            ##apply the shift
            cipher = cipher + chr(int((ord(char) - (shift))/a))

        ##else, apply the shift
        else:
            ##apply the shift
            cipher = cipher + chr(int((ord(char) - (shift))/a))
        
        
    ##return the letters
    return cipher


##-----------------------------------------------------------##


##make a loop to see if they wanna continue?
while c == True:
    
    ##ask if they wanna encrypt or decrypt
    ask = input("Would you like to encrypt a sentence, or decrypt one? e/d: ")

    ##if encrypt
    if ask == "e":
        
        ##ask for encrypted msg and shift - get your info
        ctxt = input('What is the sentence you want encrypted?:')
        s = int(input('What is the shift value?: '))
        a = int(input('Multiply value?: '))

        ##print that it was successful and the encrypted code
        print ('Encryption Successful\n')
        print ('Your encrypted sentence is:', encrypt(ctxt, s, a))

        ##ask if they want to continue
        ans = input("Would you like to go again? y/n ")

        ##yes continue
        if ans == "y":
            c = True
            
        ##no goodbye
        else:
            c = False
            print("Thank you, good bye.")


    ##if decrypt
    elif ask == "d":
        
        ##ask for encrypted msg and shift - get your info
        ctxt = input('What is your encrypted sentence?:')
        s = int(input('What is the shift value?: '))
        a = int(input('Divide value?: '))

        ##print that it was successful and the decrypted code
        print ('Decryption Successful\n')
        print ('Your decrypted sentence is:', decrypt(ctxt, s, a))

        ##ask if they want to continue
        ans = input("Would you like to go again? y/n ")

        ##yes continue
        if ans == "y":
            c = True
            
        ##no goodbye
        else:
            c = False
            print("Thank you, good bye.")

    ##if no reply
    else:
        print("Thank you, good bye.")



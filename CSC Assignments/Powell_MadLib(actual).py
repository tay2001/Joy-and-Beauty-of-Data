#Programmer: Taylor Powell
#Assignment: MadLib Exercise

#---------------------------

# ------User Inputs --------
adjective_1 = input("Input an adjective: ")
pluraln_1 = input("Input a plural noun: ")
print("Input a number:")
number_1 = int(input())
pluraln_2 = input("Input another plural noun: ")
pverb_1 = input("Input a past tense verb: ")
place = input("Input a place: ")
print("Input a decimal:")
decimal_1 = float(input())
adverb = input("Input a adverb: ")
pverb_2 = input("Input a past tense verb: ")
animal = input("Input an animal: ")
pverb_3 = input("Input another past tense verb: ")
print("Input a number:")
number_2 = int(input())
print("Input a number with a decimal:")
decimal_2 = float(input())
adjective_2 = input("Input another adjective: ")


#------- Print Story--------

print()
print("It was a "+ adjective_1 + ", hot summer day.")
print("There were no " + pluraln_1 + " in the sky, but there were " , number_1, pluraln_2 +" on the lake. ")
print("I " + pverb_1 + " to " + place + ", but " , decimal_1 , " of a second later I " + adverb, pverb_2)
print("My " + animal, pverb_3 + " to me, he has " , number_2 , " legs!")
print("I was " , decimal_2 , "% close to being " + adjective_2 + ", but now I'm not!")

print(type(number_1))

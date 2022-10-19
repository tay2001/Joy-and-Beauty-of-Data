##programmer: taylor powell
##notes: dictionaries


##-------------------------

people = {'Ryu':1,'Odin':8,'Lyra':2,'Sheldon':5}

print(people.keys())
print(people.values())
print(people.items())
print(people.get('Lyraa','does not exist'))


if 'Lyra' in people:
    print(people['Lyra'])


##convert some to list
d = list(people)
print(d)
print(type(d))

##add one to the dict
people['Stella']=0

##del one
del people['Ryu']

##change a value
people['Lyra'] = 3

##u can do math!
people['Lyra'] = people['Lyra']+5


print(people['Lyra'])


##print(type(people))
print(people)
print(len(people))



##new_list =[]
##for i in range(10):
##    new_list.append(i)
##print(new_list)
##
##
####comprehensions
##
##
##newer_list=[x**3 for x in new_list if x%2 == 0]
##
##print(new_list)
##print(newer_list)

##
##a = "hi there how are you?"
##
##b = list(a)
##
##b = a.split()
##
##
##print(b)
##print(type(b))
##
##
##glue ='yeet'
##c = glue.join(b)
##print(c)
##
##
##
##
####tuple - tuples are inmutable: cant change itself // crossover between string and list
##
##a = 2,5,"t"
##
##print(type(a))

##a =(1,2,3)
##b = ("a","b","c")
##c=(5,6,7)
##
##x = a
##y = b
##z = c
##
##b = a
##c = y
##a = z
##
####a,b,c = b,c,a
##
##print(a)
##print(b)
##print(c)

a = [[1,2],[3,4]]
for i in range(len(a)):
    print(a[i][1])

for number in a:
    print(number[1])















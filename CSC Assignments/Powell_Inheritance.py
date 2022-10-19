##programmer: taylor powell
##assignment: inheritance

##--------------------------##


##make the class

class Contact:
    """ """

    def __init__(self,first,last,phone):
        """constructor"""
        self.first = first
        self.last = last
        self.phone = phone

    def __str__(self):
        return "Name: " + str(self.first) + ' ' + str(self.last) + '\nPhone: ' + str(self.phone)  + '\n-'

    def getFirst(self):
        return self.first

    def getLast(self):
        return self.last

    def getPhone(self):
        return self.phone

    def setFirst(self, first):
        self.first = first

    def setLast(self, last):
        self.last = last

    def setPhone(self, phone):
        self.phone = phone
   

class Professional(Contact):

    def __init__(self,first,last,phone,title):
        super().__init__(first,last,phone)
        self.title = title

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def __str__(self):
        return 'Title: ' + str(self.title) + "\nName: " + str(self.first) + ' ' + str(self.last) + '\nPhone: ' + str(self.phone) +  '\n-'
    

        

class Friend(Contact):

    def __init__(self, first, last, phone, birthday):
        super().__init__(first,last,phone)
        self.birthday = birthday

    def getBirthday(self):
        return self.birthday

    def setBirthday(self, birthday):
        self.birthday = birthday

    def __str__(self):
        return 'Birthday: ' + str(self.birthday) + "\nName: " + str(self.first) + ' ' + str(self.last) + '\nPhone: ' + str(self.phone) + '\n-'
    
        
    
##revise and set them
def revContacts():

    print('My Contacts\n-------------')
    
    contact_1 = Friend('Donald','Duck','123-555-1234','Feb 28')
    contact_2 = Professional('Minnie','Mouse','406-555-4123','Mrs')
    contact_3 = Contact('Mickey','Mose','406-555-2341')
    contact_4 = Friend('Tinker','Bell','406-555-3243','???')
    contact_5 = Professional('Peter','Pan','406-555-2243','???')

    contacts = [contact_1, contact_2, contact_3, contact_4, contact_5]

    ##revise em
    ##donalds phone
    contact_1.setPhone('406-555-1234')

    ##mickeys last name
    contact_3.setLast('Mouse')

    ##Bell's birthdate
    contact_4.setBirthday('Jul 2')

    ##Peters title
    contact_5.setTitle('Mr')

    ##return the list
    return contacts

##print them all
def printContacts(contacts):
    ##varaible
    i = 0

    ##loop to print them while in the length of the list
    while i < len(contacts):
        print(contacts[i])
        i += 1



##print specific
def specificItems(contacts):
    
    print('--------------\n')
    print('Print Specific Items:\n')

    
    ##donalds
    print("Donald's birthday is" , str(contacts[0].getBirthday()))

    ##Pan
    print("Mr. Pan's Phone Number is" , str(contacts[4].getPhone()))
    



##main call em all
def main():

    ##set contacts list = to this list
    contacts = revContacts()

    ##print them all with the set list
    printContacts(contacts)

    ##print the specified items 
    specificItems(contacts)
 

    

main()

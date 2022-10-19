##10/31

class MathStuff:
    """good info"""

    def __init__(self,X,Y):
        """constructor that does math"""
        self.x = X
        self.y = Y
    def __str__(self):
        return  'x= '+ str(self.x) + ' y= ' + str(self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def mult(self):
        mult = self.x*self.y
        return mult

    def divis(self):
        divis = self.x/self.y
        return divis

    def add(self):
        add = self.x + self.y
        return add

    def sub(self):
        sub = self.x-self.y
        return sub

    def revX(self,newX):
        self.x = newX
        return self.x

    def revY(self,newY):
        self.y = newY
        return self.y


class Calc(MathStuff):

    def __init__(self,X,Y,Z):
        super().__init__(X,Y)
        self.z = Z

    def addall(self):
        return self.add()+ self.z
        

    def getZ(self):
        return self.z

    def revZ(self,newZ):
        self.z = newZ

    def __str__(self):
        return  'x='+ str(self.x) + ' y= ' + str(self.y) + ' z= ' + str(self.z)
        




prob_1 = Calc(3,5,7)
prob_2 = MathStuff(4,6)
prob_3 = Calc(4,5,6)

##print(prob_1)
print(prob_2)
##print(prob_3)
##
##
##print(prob_1.addall())
##
##print(prob_3.getZ())
##
##
##
####prob_1.revX(12)
####print(prob_1.getX())

    
    

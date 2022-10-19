##10/31/2019
##object oriented coding

class MathStuff:
    """how it alls"""

    def __init__(self,X,Y):
        """more"""
        self.x = X
        self.y = Y

    def getx(self):
        return self.x
    
    def gety(self):
        return self.y

    def mult(self):
        multi = self.x*self.y
        return multi

    def add(self):
        add = self.x+self.y
        return add
    
    def sub(self):
        sub = self.x-self.y
        return sub

    def div(self):
        div = self.x/self.y
        return div

    def revX(self, newX):
        self.x = newX

    def revY(self,):
        
        


p = MathStuff(4,4)

print(type(p))


m = p.mult()
print(m)

a = p.add()
print(a)

s = p.sub()
print(s)

d = p.div()
print(d)


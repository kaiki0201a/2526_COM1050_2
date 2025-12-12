#Lop Circle
class Circle():
    def __init__(self,x, y, r):
        self.r = r
        self.x = x
        self.y = y
        self.tam = (x, y)
    def getPerimeter(self):
        return 2 * 3.14 * (self.r)
    def getArea(self):
        return 3.14 * ((self.r)**2)
    def isIn(self, a, b):
        self.a, self.b = a, b
        if ((self.x - self.a )**2 + (self.y - self.b)**2) < (self.r )**2:
            return True
        else: return False
    def isOn(self, a, b):
        self.a, self.b = a, b
        if ((self.x - self.a )**2 + (self.y - self.b)**2) == (self.r )**2:
            return True
        else: return False
    def isOut(self, a, b):
        self.a, self.b = a, b
        if ((self.x - self.a )**2 + (self.y - self.b)**2) > (self.r )**2:
            return True
        else: return False
class Square:
    def __init__(self, a):
        self.a = a
    def getPerimeter(self):
        return a*4
    def getArea(self):
        return a*a


        
        

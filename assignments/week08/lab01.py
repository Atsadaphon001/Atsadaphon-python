class Rectangle:
    def __init__(self,length,width):
        self.__length= length
        self.__width = width
         
    def getArea(self):
        return self.__length * self.__width
    
    def getPerimeter(self):
        return 2*(self.__length + self.width)
    
    def isSquare(self):
        if self.length -- self.__width:
            return True
        else:
            return False

x = Rectangle()  
print ('Area pf x = ' + x.getArea())
print('Perimeter of x = ' + x.getPerimeter())
if x.isSquare:
    print('x = ' + x.getArea())
else:
    print('x is not square')

    
            
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        area = self.length * self.width
        return area 
    

    def get_perimeter(self):
        perimeter =  (self.length + self.width) * 2 
        return perimeter 


rect = Rectangle(10, 5)
print(rect.get_area())      
print(rect.get_perimeter())
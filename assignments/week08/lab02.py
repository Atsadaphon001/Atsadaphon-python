class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def get_info(self):
        return f"Brand : {self.brand}, Model : {self.model} , Year : {self.year}"

class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        
    def get_info(self):
        return f"Brand : {self.brand}, Model : {self.model}, Year : {self.year}, Number of doors : {self.number_of_doors}"

myCar = Car("Toyota", "Yaris Cross", 2025, 4)
print(myCar.get_info())

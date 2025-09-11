class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Fish(Animal):
    def move(self):
        print("Fish swims.")

class Bird(Animal):
    def move(self):
        print("Bird flies.")

class Dog(Animal):
    def move(self):
        print("Dog runs.")

def animal_move(animal: Animal):
    animal.move()

if __name__ == "__main__":
    animals = [Fish(), Bird(), Dog()]
    for a in animals:
        animal_move(a)
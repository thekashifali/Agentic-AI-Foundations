# Parent class
class Animal:
    def __init__(self, name, age):
        self.name = name  
        self.age = age   

    def speak(self):
        print("Some generic animal sound")  # Parent method

    def eat(self):
        print(f"{self.name} is eating")     # Common method for all animals

    def sleep(self):
        print(f"{self.name} is sleeping")   # Common method for all animals

# Dog inherits Animal
class Dog(Animal):  
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):  # Overriding parent method
        print(f"{self.name} says: Bark!")  

    def fetch(self):
        print(f"{self.name} is fetching the ball")

# Cat inherits Animal
class Cat(Animal):
    def speak(self):  # Overriding parent method
        print(f"{self.name} says: Meow!")

    def scratch(self):
        print(f"{self.name} is scratching")

# Objects
ob1 = Cat("Mano", 3)
ob2 = Dog("Buddy", 4, "Labrador")

# Access attributes (use print to see them)
print(ob1.name)  # Mano
print(ob1.age)   # 3

print(ob2.name)  # Buddy
print(ob2.age)   # 4
print(ob2.breed) # Labrador

# Call methods
ob1.speak()      # Meow!
ob2.speak()      # Bark!
ob1.eat()        # Mano is eating
ob2.eat()        # Buddy is eating

# Dog and Cat specific methods
ob2.fetch()      # Buddy is fetching the ball
ob1.scratch()    # Mano is scratching

# -------------------
# Polymorphism Example
# -------------------
def animal_speak(animal):
    animal.speak()  # Works for any object of Animal or its child classes

# Polymorphism in action
animal_speak(ob1)  # Meow!
animal_speak(ob2)  # Bark!
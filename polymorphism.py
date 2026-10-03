# ==========================================
# Python OOP - Polymorphism
# ==========================================


# 1. Same Method Name, Different Behavior
# ==========================================

class Dog:
    def sound(self):
        print("Dog says: Woof")


class Cat:
    def sound(self):
        print("Cat says: Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# ==========================================
# 2. Polymorphism with Different Objects
# ==========================================

class Car:
    def move(self):
        print("Car is driving")


class Boat:
    def move(self):
        print("Boat is sailing")


class Airplane:
    def move(self):
        print("Airplane is flying")


car = Car()
boat = Boat()
airplane = Airplane()

car.move()
boat.move()
airplane.move()


# ==========================================
# 3. Using a Function
# ==========================================

def make_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)


# ==========================================
# 4. Polymorphism with Inheritance
# ==========================================

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog says: Woof")


class Cat(Animal):

    def sound(self):
        print("Cat says: Meow")


animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.sound()
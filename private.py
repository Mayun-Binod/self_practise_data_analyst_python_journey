# ==========================================
# Python OOP - Inheritance
# ==========================================


# 1. Basic Inheritance
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()      # Inherited method
dog.bark()     # Dog's own method


# ==========================================
# 2. Inheritance with Attributes
# ==========================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def study(self):
        print(self.name, "is studying")


student = Student("Ram", 20)

student.show_person()
student.study()


# ==========================================
# 3. Child Class with Its Own Attribute
# ==========================================

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_model(self):
        print("Model:", self.model)


car = Car("Toyota", "Corolla")

car.show_brand()
car.show_model()


# ==========================================
# 4. Multiple Child Classes
# ==========================================

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat is meowing")
dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()
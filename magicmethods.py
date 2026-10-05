# ==========================================
# Python OOP - Magic Methods
# ==========================================


# 1. __init__()
# Automatically runs when an object is created
# ==========================================

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Ram", 25)

print("Name:", person.name)
print("Age:", person.age)


# ==========================================
# 2. __str__()
# Controls what is displayed when print()
# is used with an object
# ==========================================

class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Student: {self.name}, Grade: {self.grade}"


student = Student("Sita", "A")

print(student)


# ==========================================
# 3. __len__()
# Defines what len(object) should return
# ==========================================

class Team:

    def __init__(self, players):
        self.players = players

    def __len__(self):
        return len(self.players)


team = Team(["Ram", "Sita", "Hari", "Gita"])

print("\nNumber of players:", len(team))


# ==========================================
# 4. __add__()
# Defines what + does between objects
# ==========================================

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


number1 = Number(10)
number2 = Number(20)

result = number1 + number2

print("\nAddition:", result)


# ==========================================
# 5. __eq__()
# Defines how == works between objects
# ==========================================

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


person1 = Person("Ram", 25)
person2 = Person("Ram", 25)
person3 = Person("Sita", 22)

print("\nPerson 1 == Person 2:", person1 == person2)
print("Person 1 == Person 3:", person1 == person3)


# ==========================================
# 6. __lt__()
# Defines how < works between objects
# ==========================================

class Product:

    def __init__(self, price):
        self.price = price

    def __lt__(self, other):
        return self.price < other.price


product1 = Product(500)
product2 = Product(800)

print("\nProduct 1 < Product 2:", product1 < product2)


# ==========================================
# 7. __gt__()
# Defines how > works between objects
# ==========================================

print("Product 1 > Product 2:", product1 > product2)


# ==========================================
# 8. __del__()
# Runs when an object is about to be destroyed
# ==========================================

class Test:

    def __init__(self):
        print("\nObject created")

    def __del__(self):
        print("Object destroyed")


test = Test()

del test
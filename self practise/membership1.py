# Check whether "name" is a key in a student dictionary.
student = {"name": "sandhya", "age": 20, "grade": "B"}
print("name" in student)

# Check whether "age" is a key in a dictionary.
student1 = {"name": "prakriti", "age": 25, "grade": "A"}
print("age" in student1)

# Check whether "Ram" is a value in a dictionary.
student2 = {"name": "Ram", "age": 22, "grade": "C"}
print("Ram" in student2.values ())

# Check whether 101 is in a tuple of roll numbers.
roll_numbers = (100, 101, 102, 103)
print(101 in roll_numbers)

# Check whether "SQL" is in a list of subjects.
subjects = ["Math", "Science", "English", "SQL"]
print("SQL" in subjects)

# Check whether "Football" is in a list of hobbies.
hobbies = ["Reading", "Traveling", "Football", "Cooking"]
print("Football" in hobbies)

# Check whether "Kathmandu" is in a list of cities.
cities = ["Kathmandu", "Pokhara", "Biratnagar", "Lalitpur"]
print("Kathmandu" in cities)

# Check whether 500 is in a list of product prices.
product_prices = [100, 200, 300, 400, 500]
print(500 in product_prices)

# Check whether "admin" is in a list of usernames.
usernames = ["user1", "user2", "admin", "user3"]
print("admin" in usernames)

# Create your own list, tuple, set, string, and dictionary, then use both in and not in.
animals = ["Cat", "Dog", "Cow"]
print("Dog" in animals)
print("Tiger" not in animals)

# Tuple
numbers = (5, 10, 15, 20)
print(15 in numbers)
print(25 not in numbers)

# Set
fruits = {"Apple", "Banana", "Mango"}
print("Apple" in fruits)
print("Orange" not in fruits)

# String
text = "Python"
print("P" in text)
print("Z" not in text)

# Dictionary
student = {"name": "Sita","age": 21}

print("name" in student)
print("grade" not in student)
print("Sita" in student.values())
print("age" in student.keys())
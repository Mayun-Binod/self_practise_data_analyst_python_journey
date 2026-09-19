# Create a list of numbers and create a new list containing only numbers greater than 50 using a loop.
numbers = [20, 55, 10, 75, 40, 90, 30]
new_list = []
for number in numbers:
    if number > 50:
        new_list.append(number)
print(new_list)

# Create a list containing duplicate numbers and find how many times a particular number appears.
numbers = [10, 20, 10, 30, 10, 40, 20, 10]
count = 0
for i in numbers:
    if i == 10:
        count += 1
print(count)

# Create a nested list of numbers and find the sum of each inner list.
numbers = [
    [10, 20, 30],
    [5, 15, 25],
    [1, 2, 3]
]
for i in numbers:
    total = 0
    for number in i:
        total += number
    print(total)

# Create a tuple of numbers and find the largest number using a loop
numbers = (25, 10, 75, 40, 90, 30)
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest =i
print(largest)

# Create a list of tuples containing student names and marks. Access the marks of a particular student.
students = [
    ("sandhya", 80),
    ("Sunita", 75),
    ("sita", 90)
]
for i in students:
    if i[0] == "sita":
        print(i[1])

# Create a dictionary containing a student's name, subjects as a list, and marks as a tuple. Access each part separately.
student = {
    "name": "sandhya",
    "subjects": ["Python", "Java", "SQL"],
    "marks": (80, 75, 90)
}
print(student["name"])
print(student["subjects"])
print(student["marks"])

# Create a nested structure containing:
# Student name
# Age
# Subjects list
# Marks tuple
# Address dictionary

# Then access each individual value.
student = {
    "name": "sandhya",
    "age": 19,
    "subjects": ["Python", "Java", "SQL"],
    "marks": (80, 75, 90),
    "address": {
        "city": "Kathmandu",
        "country": "Nepal"
    }
}
print(student["name"])
print(student["age"])
print(student["subjects"])
print(student["marks"])
print(student["address"]["city"])
print(student["address"]["country"])

# Create a list containing 3 student dictionaries. Access and update information for any one student. solve this
students = [
    {
        "name": "sandhya",
        "age": 20,
        "marks": 80
    },
    {
        "name": "prakriti",
        "age": 21,
        "marks": 75
    },
    {
        "name": "aruna",
        "age": 22,
        "marks": 85
    }
]
print(students[1]["name"])
print(students[1]["marks"])
students[1]["age"] = 23
students[1]["marks"] = 90
print(students[1])


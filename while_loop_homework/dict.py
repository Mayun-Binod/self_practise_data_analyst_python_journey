# Create a dictionary containing name, age, and city. Print all keys.
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
for key in student:
    print(key)

# Print all values from a dictionary.
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
for value in student.values():
    print(value)

# Print both keys and values using .items().
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
for key, value in student.items():
    print(key, value)

# Create a dictionary of 5 students and their marks Print each student's name and marks.
students = {
    "sandhya": 75,
    "Sita": 45,
    "sunita": 60,
    "Gita": 35,
    "nisana": 80
}
for name, marks in students.items():
    print(name, marks)

# Print students who scored more than 50.
students = {
    "sandhya": 75,
    "Sita": 45,
    "sunita": 60,
    "Gita": 35,
    "nisana": 80
}
for name, marks in students.items():
    if marks > 50:
        print(name, marks)

# Find the total of all marks in a dictionary.
students = {
    "sandhya": 75,
    "Sita": 45,
    "sunita": 60,
    "Gita": 35,
    "nisana": 80
}
total = 0
for marks in students.values():
    total += marks
print("total:", total)

# Find the highest mark in a dictionary.
students = {
    "sandhya": 75,
    "Sita": 45,
    "sunita": 60,
    "Gita": 35,
    "nisana": 80
}
highest = 0
for marks in students.values():
    if marks > highest:
        highest = marks
print("highest mark:", highest)


# Create a dictionary containing:
# name
# age
# city
# country
student = {
    "name": "sandhyaa",
    "age": 19,
    "city": "Kathmandu",
    "country": "Nepal"
}
print(student)

# Access each value from the dictionary.
student = {
    "name": "sandhyaa",
    "age": 19,
    "city": "Kathmandu",
    "country": "Nepal"
}
print(student["name"])
print(student["age"])
print(student["city"])
print(student["country"])

# Update the age and city.
student = {
    "name": "sandhyaa",
    "age": 19,
    "city": "Kathmandu",
    "country": "Nepal"
}
student["age"] = 20
student["city"] = "pokhara"
print(student)

# Add a new key-value pair.
student = {
    "name": "sandhyaa",
    "age": 19,
    "city": "Kathmandu",
    "country": "Nepal"
}
student["course"] = "BBS"
print(student)

# Delete one key-value pair.
student = {
    "name": "sandhyaa",
    "age": 19,
    "city": "Kathmandu",
    "country": "Nepal"
}
del student["age"]
print(student)

# Create a dictionary of 5 students and their marks.
students = {
    "sandhya": 75,
    "sunita": 82,
    "prakriti": 68,
    "Sita": 90,
    "Gita": 85
}
print(students)
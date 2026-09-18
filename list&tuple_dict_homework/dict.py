# Create a dictionary containing a student's name, age, city, and course.
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu",
    "course": "BBS"
}
print(student)

# Access the value of "name" using [].
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu",
    "course": "BBS"
}
print(student["name"])

# Access the value of "age" using get().
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu",
    "course": "BBS"
}
print(student.get("age"))

# Add a new key "email" to the dictionary.
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu",
    "course": "BBS"
}
student["email"] = "sandhya@gmail.com"
print(student)

# Change the value of "age".
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu",
    "course": "BBS"
}
student["age"] = 23
print(student)

# Delete the "city" key using del.
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu",
    "course": "BBS"
}
del student["city"]
print(student)

# Delete a key using pop()
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu",
    "course": "BBS"
}
student.pop("age")
print(student)

# Remove the last key-value pair using popitem().
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu",
    "course": "BBS"
}
student.popitem()
print(student)

# Check whether "name" exists in a dictionary.
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu",
    "course": "BBS"
}
print("name" in student)

# Find the number of items using len().
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu",
    "course": "BBS"
}
print(len(student))

# Empty a dictionary using clear().
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu",
    "course": "BBS"
}
student.clear()
print(student)
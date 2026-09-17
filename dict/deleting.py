# Create a dictionary and delete one item using del.
person = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
del person["age"]
print(person)

# Delete a specific item using the pop() method.
person = {
    "name": "aruna",
    "age": 25,
    "city": "Kathmandu"
}
person.pop("age")
print(person)

# Use popitem() to remove the last inserted key-value pair.
person = {
    "name": "Binod",
    "age": 25,
    "city": "Kathmandu"
}
person.popitem()
print(person)

# Create a dictionary and remove all items using clear().
person = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
person.clear()
print(person)

# Create a dictionary of student details and delete only the "age" key.
student = {
    "name": "Ram",
    "age": 20,
    "marks": 85,
    "course": "BCA"
}
del student["age"]
print(student)








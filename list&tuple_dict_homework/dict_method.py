# Use keys() to get all keys.
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
print(student.keys())

# Use values() to get all values.
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
print(student.values())

# Use items() to get all key-value pairs.
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
print(student.items())

# Use get() to access a value.
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
print(student.get("name"))

# Use update() to change an existing value.
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
student.update({"age": 25})
print(student)

# Use update() to add a new key-value pair.
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
student.update({"email": "sandhya@gmail.com"})
print(student)

# Use setdefault() with an existing key.
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
student.setdefault("name", "sandhya")
print(student)

# Use setdefault() with a new key.
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
student.setdefault("course", "BBS")
print(student)

# Create a copy of a dictionary using copy().
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
new_student = student.copy()
print(new_student)

# Use pop() to remove a specific key.
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
student.pop("age")
print(student)

# Use popitem() to remove the last item.
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
student.popitem()
print(student)

# Use clear() and check the output.
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
student.clear()
print(student)
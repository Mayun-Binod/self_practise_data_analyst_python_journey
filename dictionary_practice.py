# Create a dictionary called student with name, age, address, and course. Print the dictionary.
student = {
    "name": "sandhya oli",
    "age": 19,
    "address": "Kathmandu",
    "course": "BBS"}
print(student)

# Create a dictionary with 3 items and print the value of a specific key.
student1 = {
    "name": "sandhya oli",
    "age": 19,
    "course": "BBS"}
print(student1["name"])

# Add a new key-value pair to an existing dictionary.
student2 = {
    "name": "sandhya oli",
    "age": 19}
student2["address"] = "Kathmandu"
print(student2)

# Update the value of an existing key in a dictionary.
studentt = {
    "name": "sandhya oli",
    "age": 19}
studentt["age"] = 20
print(studentt)

# Delete one item from a dictionaryDelete one item from a dictionary
student3 = {
    "name": "sandhya oli",
    "age": 19,
    "course": "BBS"}
del student3["age"]
print(student3)

# Check whether a particular key exists in a dictionary
student = {
    "name": "sandhya",
    "age": 20,
    "course": "BBs"}
if "name" in student:
    print("Key exists")
else:
    print("Key does not exist")


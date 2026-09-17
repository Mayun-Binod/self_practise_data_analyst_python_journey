# Create a dictionary containing a person's name, age, and city. Access and print the name.
person = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
print(person["name"])

# Create a dictionary containing 5 student details. Access the value of a specific key using square brackets [].
student = {
    "name": "prakriti",
    "age": 20,
    "city": "Kathmandu",
    "course": "BBS",
    "marks": 80
}
print(student["course"])

# Create a dictionary of fruits and prices. Access the price of "apple".
fruits = {
    "apple": 150,
    "banana": 100,
    "mango": 200
}
print(fruits["apple"])

# Create a nested dictionary containing student information. Access the student's name.
student = {
    "student1": {
        "name": "Ram",
        "age": 20,
        "marks": 85
    }
}
print(student["student1"]["name"])

# Create a dictionary and access a value using the get() method.
person = {
    "name": "sandhya",
    "age": 19,
    "city": "kathmandu"
}
print(person.get("age"))

# Create a dictionary and try accessing a key that does not exist using both [] and get(). Observe the difference.
person = {
    "name": "sandhya",
    "age": 25
}
print(person["city"])
print(person.get("city"))




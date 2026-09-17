# Create a dictionary containing a person's name, age, and city. Update the person's age.
person = {
    "name": "sandhya",
    "age": 19,
    "city":"kathmandu"

}
person["age"] = 19
print(person)

# Create a dictionary of product prices and update the price of one product.
products = {
    "laptop": 80000,
    "phone": 50000,
    "mouse": 15000
}
products["phone"] = 55000
print(products)

# Create a student dictionary containing name, age, and marks. Update the marks.
student = {
    "name": "aruna",
    "age": 19,
    "marks": 75
}
student["marks"] = 85
print(student)

# Add a new key-value pair to an existing dictionary.
person = {
    "name": "prakriti",
    "age": 22
}
person["city"] = "Kathmandu"
print(person)

# Update two existing values in a dictionary.
# 11
person = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu"
}
person["age"] = 26
person["city"] = "Pokhara"
print(person)

# Use the update() method to add multiple key-value pairs to a dictionary.
person = {
    "name": "Binod",
    "age": 25
}
person.update({
    "city": "Kathmandu",
    "course": "BCA"
})
print(person)

# Use update() to change an existing value and add a new key at the same time.
person = {
    "name": "nisana",
    "age": 25
}
person.update({
    "age": 26,
    "city": "Kathmandu"
})
print(person)



# Create a dictionary containing:
# name
# age
# city
# course
# marks

# Perform these operations:
# Access name
# Access marks
# Update age
# Update marks
# Add email
# Delete city
# Print the final dictionary
student = {
    "name": "sandhya",
    "age": 19,
    "city": "Kathmandu",
    "course": "BBS",
    "marks": 70
}
print(student["name"])
print(student["marks"])
student["age"] = 20
student["marks"] = 80
student["email"] = "sandhya@gmail.com"
del student["city"]
print(student)

# Create a product dictionary containing name, price, quantity, and category Access, update, add, and delete different values
product = {
    "name": "Laptop",
    "price": 80000,
    "quantity": 5,
    "category": "Electronics"
}
print(product["name"])
print(product["price"])
product["price"] = 75000
product["quantity"] = 10
product["brand"] = "Dell"
del product["category"]
print(product)

# Create a student dictionary. Access a value, update the marks, add a new key called grade, and delete the age.
student = {
    "name": "sandhya",
    "age": 20,
    "marks": 75
}
print(student["name"])
student["marks"] = 85
student["grade"] = "A"
del student["age"]
print(student)

# Create a nested dictionary containing information about two students. Access one student's marks, update the marks, and delete one student's city. solve this
students = {
    "student1": {
        "name": "sandhya",
        "age": 19,
        "city": "Kathmandu",
        "marks": 75
    },
    "student2": {
        "name": "binod",
        "age": 25,
        "city": "Pokhara",
        "marks": 80
    }
}
print(students["student1"]["marks"])
students["student1"]["marks"] = 85
del students["student2"]["city"]
print(students)








# Create a dictionary containing information about three students using nested dictionaries.
students = {
    "student1": {
        "name": "sandhya",
        "age": 19,
        "city": "Kathmandu"
    },
    "student2": {
        "name": "prakrit",
        "age": 23,
        "city": "Pokhara"
    },
    "student3": {
        "name": "binod",
        "age": 24,
        "city": "Chitwan"
    }
}
print(students)

# Access the name of the first student.
students = {
    "student1": {
        "name": "sandhya",
        "age": 19,
        "city": "Kathmandu"
    },
    "student2": {
        "name": "prakrit",
        "age": 23,
        "city": "Pokhara"
    },
    "student3": {
        "name": "binod",
        "age": 24,
        "city": "Chitwan"
    }
}
print(students["student1"]["name"])

# Access the age of the second student.
students = {
    "student1": {
        "name": "sandhya",
        "age": 19,
        "city": "Kathmandu"
    },
    "student2": {
        "name": "prakrit",
        "age": 23,
        "city": "Pokhara"
    },
    "student3": {
        "name": "binod",
        "age": 24,
        "city": "Chitwan"
    }
}
print(students["student2"]["age"])

# Change the city of the third student.
students = {
    "student1": {
        "name": "sandhya",
        "age": 19,
        "city": "Kathmandu"
    },
    "student2": {
        "name": "prakrit",
        "age": 23,
        "city": "Pokhara"
    },
    "student3": {
        "name": "binod",
        "age": 24,
        "city": "Chitwan"
    }
}
students["student3"]["city"] = "Lalitpur"
print(students)

# Add a new key "grade" to one student's nested dictionary.
students = {
    "student1": {
        "name": "sandhya",
        "age": 19,
        "city": "Kathmandu"
    },
    "student2": {
        "name": "prakrit",
        "age": 23,
        "city": "Pokhara"
    },
    "student3": {
        "name": "binod",
        "age": 24,
        "city": "Chitwan"
    }
}
students["student1"]["grade"] = "A"
print(students)

# Delete one key from a nested dictionary.
students = {
    "student1": {
        "name": "sandhya",
        "age": 19,
        "city": "Kathmandu"
    },
    "student2": {
        "name": "prakrit",
        "age": 23,
        "city": "Pokhara"
    },
    "student3": {
        "name": "binod",
        "age": 24,
        "city": "Chitwan"
    }
}
del students["student2"]["city"]
print(students)

# Use get() to access a value inside a nested dictionary.
students = {
    "student1": {
        "name": "sandhya",
        "age": 19,
        "city": "Kathmandu"
    },
    "student2": {
        "name": "prakrit",
        "age": 23,
        "city": "Pokhara"
    },
    "student3": {
        "name": "binod",
        "age": 24,
        "city": "Chitwan"
    }
}
print(students["student1"].get("age"))

# Use update() to change a value inside a nested dictionary.
students = {
    "student1": {
        "name": "sandhya",
        "age": 19,
        "city": "Kathmandu"
    },
    "student2": {
        "name": "prakrit",
        "age": 23,
        "city": "Pokhara"
    },
    "student3": {
        "name": "binod",
        "age": 24,
        "city": "Chitwan"
    }
}
students["student3"].update({"age": 25})
print(students)
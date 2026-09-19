# Create a list containing tuples and access an item inside one tuple.
my_list = [("sandhya", 20), ("binod", 25), ("sunita", 30)]
print(my_list[1][1])

# Create a tuple containing lists and change an item inside one list.
tuple = (["apple", "banana"], ["cat", "dog"])
tuple[0][1] = "mango"
print(tuple)

# Create a list containing dictionaries and access a value from one dictionary.
students = [
    {"name": "sandhya", "age": 20},
    {"name": "prakriti", "age": 22}
]
print(students[1]["name"])

# Create a dictionary containing lists as values and access one list item.
student = {
    "name": "sandhya",
    "subjects": ["math", "english", "science"]
}
print(student["subjects"][1])

# Create a dictionary containing tuples as values and access one tuple item.
student = {
    "name": "sandhya",
    "marks": (80, 75, 90)
}
print(student["marks"][2])

# Create a nested list containing dictionaries and access a dictionary value.
students = [
    [
        {"name": "sandhya", "age": 20},
        {"name": "prakriti", "age": 22}
    ]
]
print(students[0][1]["age"])

# Create a nested dictionary containing lists and access one list item.
students = {
    "student1": {
        "name": "Ram",
        "subjects": ["Python", "Java", "SQL"]
    }
}
print(students["student1"]["subjects"][2])

# Create a list of student dictionaries and update one student's age.
students = [
    {"name": "sandhya", "age": 20},
    {"name": "prakriti", "age": 22},
    {"name": "sunita", "age": 30}
]
students[1]["age"] = 25
print(students)

# Create a dictionary where one key contains a list of 5 subjects. Add another subject to that list.
student = {
    "name": "sandhya",
    "subjects": ["Python", "english", "math", "SQL", "science"]
}
student["subjects"].append("eco")
print(student)




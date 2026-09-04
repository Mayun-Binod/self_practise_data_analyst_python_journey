# Create a dictionary containing information about an employee: name, age, position, salary, and city.
employee = {
    "name": "sandhya",
    "age": 19,
    "position": "Data Analyst",
    "salary": 50000,
    "city": "Kathmandu"}
print(employee)

# Add a new employee detail to the dictionary.
employee1 = {
    "name": "sandhya",
    "age": 19,
    "position": "Data Analyst",
    "salary": 50000,
    "city": "Kathmandu"}
print(employee1)
employee1["experience"] = "2 years"
print(employee1)


#Update the employee's salary
employee2 = {
    "name": "sandhya",
    "age": 19,
    "position": "Data Analyst",
    "salary": 50000,
    "city": "Kathmandu"}
employee2["salary"] = 60000
print(employee2)

# 4. Delete the employee's age
employee3 = {
    "name": "sandhya",
    "age": 19,
    "position": "Data Analyst",
    "salary": 50000,
    "city": "Kathmandu"}
del employee3["age"]
print(employee3)

# Create a nested dictionary containing information about two students.
students = {
    "student1": {
        "name": "prakrriti",
        "age": 20,
        "marks": 85
    },
    "student2": {
        "name": "nisana",
        "age": 21,
        "marks": 90
    }
}
print(students)

# Create a dictionary containing 5 students and their marks. Use a loop to print their names and marks. solve this
students_marks = {
    "Ram": 85,
    "Shyam": 90,
    "Hari": 78,
    "Sita": 92,
    "Gita": 88
}
for name, marks in students_marks.items():
    print(name, marks)

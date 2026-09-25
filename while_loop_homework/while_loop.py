# Print all keys and values of a dictionary using a while loop.
students = {
    "sandhya": 75,
    "Sita": 45,
    "sunita": 60
}
keys = list(students.keys())
i = 0
while i < len(keys):
    key = keys[i]
    print(key, students[key])
    i += 1

# Print only the values of a dictionary using a while loop.
students = {
    "sandhya": 75,
    "Sita": 45,
    "sunita": 60
}
keys = list(students.keys())
i = 0
while i < len(keys):
    print(students[keys[i]])
    i += 1

# Search for a particular key using a while loop.
students = {
    "sandhya": 75,
    "Sita": 45,
    "sunita": 60
}
search = "Sita"
keys = list(students.keys())
i = 0
while i < len(keys):
    if keys[i] == search:
        print("Key found")
        break
    i += 1

# Print dictionary items one by one using a while loop.
students = {
    "sandhya": 75,
    "Sita": 45,
    "sunita": 60
}
keys = list(students.keys())
i = 0
while i < len(keys):
    key = keys[i]
    print(key, students[key])
    i += 1

# Stop the loop when a particular key is found using break.
students = {
    "sandhya": 75,
    "Sita": 45,
    "Hari": 60,
    "Gita": 80
}
keys = list(students.keys())
i = 0
while i < len(keys):
    if keys[i] == "Hari":
        print("Hari found")
        break
    print(keys[i], students[keys[i]])
    i += 1

# Skip a particular dictionary item using continue.
students = {
    "sandhya": 75,
    "Sita": 45,
    "Hari": 60,
    "Gita": 80
}
keys = list(students.keys())
i = 0
while i < len(keys):
    if keys[i] == "Hari":
        i += 1
        continue
    print(keys[i], students[keys[i]])
    i += 1
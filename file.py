# ==========================================
# Python File Handling
# ==========================================


# 1. Create and Write to a File
# ==========================================

file = open("student.txt", "w")

file.write("Name: Ram\n")
file.write("Age: 20\n")
file.write("Grade: A\n")

file.close()

print("File created and data written successfully.")


# ==========================================
# 2. Read the File
# ==========================================

file = open("student.txt", "r")

data = file.read()

print("\nFile Content:")
print(data)

file.close()


# ==========================================
# 3. Append Data to the File
# ==========================================

file = open("student.txt", "a")

file.write("Course: BCA\n")

file.close()

print("New data added successfully.")


# ==========================================
# 4. Read Line by Line
# ==========================================

file = open("student.txt", "r")

print("\nReading Line by Line:")

for line in file:
    print(line.strip())

file.close()


# ==========================================
# 5. Using with Statement
# ==========================================

with open("student.txt", "r") as file:

    data = file.read()

    print("\nUsing with Statement:")
    print(data)


# ==========================================
# 6. Write Multiple Lines
# ==========================================

students = [
    "Ram - 20\n",
    "Sita - 21\n",
    "Hari - 22\n"
]

with open("students.txt", "w") as file:

    file.writelines(students)

print("Multiple students added successfully.")
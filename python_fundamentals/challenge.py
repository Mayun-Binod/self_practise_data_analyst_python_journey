# Create a simple student result program that:
# Takes student name as input.
# Takes marks of 5 subjects.
# Calculates total and average.
# Assigns a grade using if/elif/else.
# Checks whether the student passed or failed.
# Uses a loop to process the subjects.
# Stores the subjects and marks in a list or dictionary. solve this
student_name = input("Enter student name: ")
subjects = ["English", "Math", "Science", "Computer", "Nepali"]
marks = { }
total = 0
for subject in subjects:
    mark = float(input(f"Enter marks for {subject}: "))
    marks[subject] = mark
    total += mark
average = total / len(subjects)
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

if average >= 40:
    result = "Passed"
else:
    result = "Failed"
print("\n--- Student Result ---")
print("Name:", student_name)
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)
print("Result:", result)
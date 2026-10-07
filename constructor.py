# ==========================================
# Constructor in Python
# One File Example
# ==========================================


# Create a Student class
class Student:

    # Constructor
    # It runs automatically when an object is created
    def __init__(self, name, age, grade):

        # Store the given values in object attributes
        self.name = name
        self.age = age
        self.grade = grade

    # Method to display student information
    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)


# Create the first object
student1 = Student("Binod", 25, "A")

# Create the second object
student2 = Student("Ram", 22, "B")


# Display information
print("Student 1")
student1.show_info()

print("\nStudent 2")
student2.show_info()
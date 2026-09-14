# Create two strings and concatenate them using +.
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

# Create a name string and an age integer. Concatenate them into one sentence using str().
name = "Binod"
age = 25
result = "My name is " + name + " and I am " + str(age) + " years old."
print(result)

# Create a string and a float value. Concatenate them using str().
course = "My GPA is"
gpa = 3.37
result = course + " " + str(gpa)
print(result)

# Create a string and a Boolean value. Concatenate them using str().
status = "Student status:"
is_student = True
result = status + " " + str(is_student)
print(result)

# Create two lists containing numbers and concatenate them using +.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)

# Create two lists containing different data types and concatenate them.
list1 = [1, "Hello", 3.5]
list2 = [True, "Python", 10]
result = list1 + list2
print(result)

# Create two tuples and concatenate them using +.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)

# Create a string, integer, float, and Boolean. Convert the non-string values to strings and concatenate all four into one sentence.
name = "Binod"
age = 25
gpa = 3.37
is_student = True
result = "Name: " + name + ", Age: " + str(age) + ", GPA: " + str(gpa) + ", Student: " + str(is_student)
print(result)

# Create:
# first_name = "Binod"
# last_name = "Shrestha"
# age = 25
# gpa = 3.37
# Concatenate all values into one sentence using + and str().
first_name = "Binod"
last_name = "Shrestha"
age = 25
gpa = 3.37
result = "My name is " + first_name + " " + last_name + ", I am " + str(age) + " years old and my GPA is " + str(gpa) + "."
print(result)

# Try to concatenate a string and an integer without using str(). Observe the error and then correct it.
name = "Binod"
age = 25
result = name + " " + str(age)
print(result)

# Create two lists and one tuple. Concatenate the two lists and concatenate the two tuples separately.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
tuple1 = ("A", "B")
tuple2 = ("C", "D")
list_result = list1 + list2
tuple_result = tuple1 + tuple2
print(list_result)
print(tuple_result)

# Create a list containing strings and another list containing integers. Concatenate both lists into one list.
name = "Binod"
age = 25
city = "Kathmandu"
gpa = 3.37
result = "My name is " + name + ", I am " + str(age) + " years old, I live in " + city + ", and my GPA is " + str(gpa) + "."
print(result)
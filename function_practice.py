# Write a function that takes a student's marks and returns the grade.
def grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

result = grade(75)
print(result)

# Write a function that takes length and width and returns the area of a rectangle.
def rectangle_area(length, width):
    return length * width

result = rectangle_area(10, 5)
print(result)

# Write a function that takes the radius of a circle and returns its area.
def circle_area(radius):
    pi = 3.14
    return pi * radius * radius

result = circle_area(5)
print(result)

# Write a function that takes principal, rate, and time and returns simple interest.
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

result = simple_interest(10000, 5, 2)
print(result)

# Write a function that takes a person's age and returns whether they are eligible to vote.
def voting_age(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

result = voting_age(20)
print(result)

# Write a function that takes three numbers and returns the largest number. solve this
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

result = largest(10, 25, 15)
print(result)
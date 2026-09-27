# Check whether a number is positive, negative, or zero.
number = 10
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Check whether a number is even or odd.
number = 12
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Take two numbers and print the greater number.
a = 25
b = 40
if a > b:
    print(" a is greater")
elif b > a:
    print(" b is greater")
else:
    print("Both are equal")

# Take three numbers and print the greatest number.
a = 25
b = 40
c = 30
if a >= b and a >= c:
    print("a is greatest")
elif b >= a and b >= c:
    print("b is greatest")
elif c >=a and c>=b:
    print("c is greatest")
else:
    print("is greatest")

# Check whether a person is eligible to vote.
age = 20
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Create a grading system using marks:
# 80–100 → A
# 70–79 → B
# 60–69 → C
# 50–59 → D
# Below 50 → F
marks = 75
if marks >= 80 and marks <= 100:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:
    print("Grade F")
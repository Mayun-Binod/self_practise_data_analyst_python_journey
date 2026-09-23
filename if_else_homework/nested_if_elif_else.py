# Create a login system using username and password. If the username is correct, check the password.
username = "sandhya"
password = "1234"
if username == "sandhya":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")

# Create a student result system. First check whether the student passed. If they passed, check their grade.
marks = 75
if marks >= 40:
    if marks >= 80:
        print("Grade A")
    elif marks >= 60:
        print("Grade B")
    elif marks >= 50:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("Failed")

# Take a person's age. If they are eligible to vote, check whether they have a valid ID.
age = 20
card = "yes"
if age >= 18:
    if card == "yes":
        print("You can vote")
    else:
        print("required")
else:
    print("not eligible to vote")

# Take a number. First check whether it is positive. If positive, check whether it is even or odd.
number = 18
if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("negative")

# Take a person's age and citizenship status. First check the age, then check citizenship.
age = 25
citizenship = "yes"
if age >= 18:
    if citizenship == "yes":
        print("Eligible")
    else:
        print("Citizenship required")
else:
    print(" requirement failed")

# Take a student's marks. If marks are 40 or above, use another condition to classify the grade.
marks = 67
if marks >= 40:
    if marks >= 80:
        print("Grade A")
    elif marks >= 60:
        print("Grade B")
    elif marks >= 50:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("Failed")

#Create a simple ATM login system:
# Check PIN
#  If PIN is correct, check balance
# If balance is sufficient, allow withdrawal
pin = 1234
balance = 50000
amount = 10000
if pin == 1234:
    if amount <= balance:
        print("successful.")
        print("balance:", balance - amount)
    else:
        print("Insufficient balance.")
else:
    print("Incorrect PIN.")

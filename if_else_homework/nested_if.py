# Take a person's age. If they are 18 or older, check whether they are 21 or older.
age = 22
if age >= 18:
    if age >= 21:
        print("21 or older.")
    else:
        print(" under 21.")
else:
    print("under 18.")

# Take a number. If it is positive, check whether it is even or odd.
number = 20
if number > 0:
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
else:
    print("not positive")

# Take a number. If it is greater than 10, check whether it is greater than 20.
number1 = 25
if number1 > 10:
    if number1 > 20:
        print("Greater than 20")
    else:
        print("not greater than 20")
else:
    print("less")
# Take marks. If the student has passed, check whether they received a distinction.
marks = 85
if marks >= 40:
    if marks >= 80:
        print("distinction")
    else:
        print("Passed")
else:
    print("Failed")

# Take a username. If the username is correct, check the password.
username = "sandhya"
password = "1234"
if username == "sandhya":
    if password == "1234":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")

# Take a person's age. If they are 18 or older, check whether they have an ID card.
age = 20
card = "yes"
if age >= 18:
    if card == "yes":
        print("enter.")
    else:
        print("required.")
else:
    print("under 18.")

# Take a number. If it is divisible by 2, check whether it is also divisible by 4.
number2 = 12
if number2 % 2 == 0:
    if number2 % 4 == 0:
        print("both 2 and 4.")
    else:
        print("not by 4.")
else:
    print("Not divisible by 2.")
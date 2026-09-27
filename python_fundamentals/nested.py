# Check whether a number is positive. If positive, check whether it is even or odd.
number = 20
if number > 0:
    if number % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    print("Number is not positive")

# Take age and citizenship as input. Check whether the person is eligible to vote.
age = 20
citizenship = "yes"
if age >= 18:
    if citizenship == "yes":
        print("Eligible to vote")
    else:
        print("Not eligible to vote")
else:
    print("below 18")

# Take username and password. Check whether both are correct.
username = "sandhya"
password = "1234"
if username == "sandhya":
    if password == "1234":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")


# Check whether a person is eligible for a job based on:
# Age >= 18
# Education = "Bachelor"
# Experience >= 1 year
age = 25
education = "Bachelor"
experience = 2
if age >= 18:
    if education == "Bachelor":
        if experience >= 1:
            print("Eligible the job")
        else:
            print("At least 1 year experience")
    else:
        print("Bachelor degree is required")
else:
    print("Age 18 or above")

# Create a login system using:
# Username
# Password
# Account status
username = "sandhya"
password = "1234"
status = "active"
if username == "sandhya":
    if password == "1234":
        if status == "active":
            print("Login successful.")
        else:
            print("Account is inactive.")
    else:
        print("Incorrect password.")
else:
    print("Incorrect username.")

# Check whether a student is eligible for admission based on:
# Marks >= 60
# Age >= 18
# Entrance exam passed
marks = 70
age = 20
entrance = "yes"
if marks >= 60:
    if age >= 18:
        if entrance == "yes":
            print("Eligible for admission.")
        else:
            print("not passed")
    else:
        print(" requirement")
else:
    print("60 or above")

# Create a driving-license eligibility program using:
# Age
# Citizenship
# Valid documents
age = 20
citizenship = "yes"
documents = "yes"
if age >= 18:
    if citizenship == "yes":
        if documents == "yes":
            print("Eligible for driving license.")
        else:
            print("required")
    else:
        print("Citizenship required")
else:
    print("18 or older")

# Create a shopping discount system based on:
# Purchase amount
# Membership status
amount = 8000
membership = "yes"
if membership == "yes":
    if amount >= 10000:
        discount = amount * 0.20
    elif amount >= 5000:
        discount = amount * 0.10
    else:
        discount = amount * 0.05
else:
    if amount >= 10000:
        discount = amount * 0.10
    else:
        discount = 0
print("Discount:", discount)
print("Final amount:", amount - discount)
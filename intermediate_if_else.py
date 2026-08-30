# Take marks and display the grade:
# 80+ → A
# 70–79 → B
# 60–69 → C
# 40–59 → D
# Below 40 → Fail
marks = float(input("Enter your marks: "))
if marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")

# Take a number and check whether it is divisible by 3, divisible by 5, or divisible by both.
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("Divisible by both 3 and 5")
elif number % 3 == 0:
    print("Divisible by 3")
elif number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")

# Take three numbers and find the largest number.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)
else:
    print("Largest number is:", num3)

# Take a person's age and classify them as Child, Teenager, Adult, or Senior.
age = int(input("Enter your age: "))
if age < 15:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# Take a temperature and display Cold, Normal, Hot, or Very Hot.
temperature = float(input("Enter temperature: "))
if temperature < 10:
    print("Cold")
elif temperature < 25:
    print("Normal")
elif temperature < 35:
    print("Hot")
else:
    print("Very Hot")

# Take a day number (1–7) and display the day name.
day = int(input("Enter day number (1-7): "))
if day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursday")
elif day == 6:
    print("Friday")
elif day == 7:
    print("Saturday")
else:
    print("Invalid day number")


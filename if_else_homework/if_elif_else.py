# Take marks and print:
# 80–100 → A
# 60–79  → B
# 40–59  → C
# Below 40 → Fail
marks = 75
if marks >= 80 and marks <= 100:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 40:
    print("C")
else:
    print("Fail")

# Take a number and check whether it is positive, negative, or zero.
number = -10
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Take a person's age and classify them as:
# 0–12 → Child
# 13–19 → Teenager
# 20–59 → Adult
# 60+ → Senior
age = 25
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")

# Take a number and print whether it is 1, 2, 3, or another number.
number1 = 3
if number1 == 1:
    print("One")
elif number1 == 2:
    print("Two")
elif number1 == 3:
    print("Three")
else:
    print("Another number")

# Take a day number from 1–7 and print the corresponding day.
day = 7
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
    print("other day")

# Take a month number and print the corresponding month.
month = 9
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("other month")

# Take a temperature and classify it as cold, normal, or hot.
temperature = 25
if temperature < 15:
    print("Cold")
elif temperature <= 30:
    print("Normal")
else:
    print("Hot")

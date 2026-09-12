# # x = int(input("Enter the number:"))
# # if x > 10:
# #   print("greater than 10")
# #   if x > 20:
# #     print("greater than 20")
# #   else:
# #     print("but not above 20.")
# # else:
# #   print("greater than 10.")


# # 
# age = int(input("Enter the age:"))
# has_license = True

# if age >= 18:
#   if has_license:
#     print("You can drive")
#   else:
#     print("You need a license")
# else:
#   print("You are too young to drive")

# # 
# if age >= 20:
#   if not has_license:
#     print("You can drive")
#   else:
#     print("You need a license")
# else:
#   print("You are too young to drive")


score = int(input("Enter the score:"))
attendance = int(input("Enter the attendance:"))
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")


day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
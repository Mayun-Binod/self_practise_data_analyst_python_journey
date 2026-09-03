employee_details = {
    "employee_id": 101,
    "employee_name": "sandhya oli",
    "employee_age" : 19,
    "employee_position" : "manager",
    "employee_department": "IT",
    "employee_salary": 50000,
    "employee_phone_number": "9762637995",
    "employee_email": "sandhya@gmail.com",
    "employee_address": "ranibari"
}
print(employee_details)

# UPDATE/////
employee_details["employee_name"] = "Binod Shrestha"
print(employee_details)

# DELETE///
del employee_details["employee_age"]
print(employee_details)


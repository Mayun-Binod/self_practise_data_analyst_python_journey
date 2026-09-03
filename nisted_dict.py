bank_details = {
    "account_holder": {
        "account_number": "1234567890",
        "name": "Sandhya Oli",
        "age": 19},
      "account_info": {"account_type": "Savings",
        "branch": "Kathmandu"},
    "contact_info": {"phone": "9863624556",
        "email": "sandhya@gmail.com",
        "address": "ranibari" }}

print(bank_details["account_holder"]["account_number"])
print(bank_details["account_info"]["account_type"])
print(bank_details["contact_info"]["phone"])

#  UPDATE////
bank_details["contact_info"]["phone"] = "9762637995"
print(bank_details)

del bank_details["account_holder"]["age"]
print(bank_details)
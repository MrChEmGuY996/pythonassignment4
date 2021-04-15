# Enter the price of the house you wish to buy
price = int(input("Enter the house price:"))

# Enter the credit score
credit_score = int(input("Enter credit score:"))

# Enter the first name
first_name = input("Enter first name:")

# Enter the last name
last_name = input("Enter last name:")

full_name = (first_name + " " + last_name)

# Enter the email
email = input("Enter E-mail:")

# Enter the phone number
phone_number = input("Enter phone number:")

# Enter the mailing
mailing_address1 = input("Enter mailing address:")
mailing_address2 = input("Enter City:")
mailing_address3 = input("Enter State:")
mailing_address4 = input("Enter Zip code:")

# Qualify for loans with the best interest rates
if credit_score >= 780 and 850:
    credit_status = "Excellent Credit Score"
    print("Zero Down Payment")
    down_payment = 0.0 * price

# Usually qualify for loans with the best interest rates
elif credit_score >= 740 and 779:
    credit_status = "Very Good Credit Score"
    down_payment = 0.02 * price

# May face loans with higher interest rates
elif credit_score >= 720 and 739:
    credit_status = "Above Average Credit Score"
    down_payment = 0.03 * price

# May qualify for most loans with higher interest rates
elif credit_score >= 680 and 719:
    credit_status = "Average Credit Score"
    down_payment = 0.06 * price

# May qualify for most loans with really high interest rates
elif credit_score >= 620 and 679:
    credit_status = "Below Average Credit Score"
    down_payment = 0.18 * price

# Usually has some credit issues; will probably not qualify for most loans
elif credit_score >= 580 and 619:
    credit_status = "Poor Credit Score"
    down_payment = 0.20 * price

# Facing extreme credit issues
elif credit_score <= 520 :
    credit_status = "Poor Credit Score"
    down_payment = 0.25 * price

print("Full name: " + full_name)
print("Physical address: " + mailing_address1)
print("City: " + mailing_address2 + ", State: " + mailing_address3 + ", Zipcode: " + mailing_address4)
print("New House Price: $" + str(price))
print("Down Payment: $" + str(down_payment))
print("Credit score: " + str(credit_score))
print("Credit Status: " + str(credit_status))






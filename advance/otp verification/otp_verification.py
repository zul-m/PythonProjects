# Import the necessary Python libraries.
import os
import math
import random
import smtplib

# Generate a random number and store it in a variable.
digits = "0123456789"
OTP = ""

for i in range(6):
    OTP += digits[math.floor(random.random()*10)]

otp = OTP + " is your OTP number."
msg = otp

# Use key from Gmail account to send email for OTP verification.
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Your Gmail account", "Your app password")
email_id = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&', email_id, msg)

a = input("Enter you OTP number: ")

if a == OTP:
    print("OTP Verified!")
else:
    print("Please check your OTP number again.")
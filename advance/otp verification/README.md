## OTP Verification

Do you know how you get a unique OTP every time you go through the payment process in an online transaction? Each company has its ways of creating an OTP for verification, but most of the companies have their systems programmed to generate a 6-digit random number.

### Steps to Create an OTP Verification System using Python

OTP Verification is the process of verifying a user by sending a unique password so that the user can be verified before completing a registration or payment process. Most of the time, we get an OTP when we make an online payment, or when we forget our password, or when creating an account on any online platform. Thus, the sole purpose of an OTP is to verify the identity of a user by sending a unique password.

We can easily create an application for the task of OTP verification using Python by following the steps mentioned below:
 1. First, create a 6-digit random number
 2. Then store the number in a variable
 3. Then we need to write a program to send emails
 4. When sending email, we need to use OTP as a message
 5. Finally, we need to request two user inputs; first for the user’s email and then for the OTP that the user has received.

So this is the complete process of creating an OTP verification application using Python.

### OTP Verification using Python

I start by importing the necessary Python library that we need for this task. Then, I generate a random number and store it in a variable which I will be using while sending emails to the users. You need to have your Google app password to be able to send emails using your Gmail account. For this task, you need to follow the steps mentioned [here](https://support.google.com/accounts/answer/185833?hl=en). After you create your app password for your Gmail account you will get a key. Copy that key and paste in the code to send emails for OTP verification using Python.

Once you run the code you enter an email where you want to send an OTP and then enter the OTP that you have received in the email.

### Output

```
Enter your email: 
Enter you OTP number: 057749
OTP Verified!
```

```
Enter your email: 
Enter you OTP number: 166089
Please check your OTP number again.
```

### Summary

So this is how you can create an application for your task of OTP verification. The next thing that you can do is use this logic to create the same application in a form of a user interface.
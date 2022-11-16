## Generate Password

To create a password with Python, we need to create a program that takes the length of the password and generates a random password of the same length. In this project, I’ll walk you through how to write a Python program to generate a password.

### Python Program to Generate Password

To write a Python program to create a password, declare a string of numbers + uppercase + lowercase + special characters. Take a random sample of the string of a length given by the user.

In the code, I first imported the `random` module in Python, then I asked for user input for the length of the password. Then I stored the letters, numbers and special characters that I want to be considered while generating a password. Then I am doing a random sampling by joining the length of the password and the variable `s`, which will finally generate a random password.

### Output

```
Enter the length of password: 8
LBb?e!kF
```

### Summary

There are a few areas where the code could be improved upon, but at a basic level, it meets many secure password generation requirements by today’s standards. As a newbie to Python or any other language, you should keep trying these types of programs as they help you explore more functions and in the long run will help you design your algorithms.
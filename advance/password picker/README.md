## Password Picker

A password picker is an application that allows you to create strong passwords by combining words, numbers, and special characters. A password picker will create a new password and show it to you every time you run your program which is the main logic behind creating a password picker with Python.

Your program should keep creating a new password again and again until you find a strong and easy to remember.

A password picker randomly selects each of the four criteria i.e. adjective, name, number, special character and puts them together to create a strong password and display it on the screen. In the process, if you want another password, the program will repeat the steps, and if you no longer need a new password, the program will end.

### Password Picker with Python

I created a password picker with Python using the `random` module. Our program should use random choices from the group of adjectives, nouns, numbers, and special characters. Now let’s see how to create a password picker with Python.

I start by importing the `random` module in Python. Then I print a welcome message to the user, and start generate a random password.

### Output

```
Welcome to Password Picker
Your password is: fatdinosaur71~
Would you like another password? Type Y or N >> Y
Your password is: bluehammer31*
Would you like another password? Type Y or N >> Y
Your password is: sleepydragon27_
Would you like another password? Type Y or N >> N
```

### Summary

This application can personally help you to create strong passwords.
## Password Authentication

Password Authentication is the process of checking the identity of a user. Almost every online platform today makes sure that they only give access to the real user which can be only possible by asking for a password while a user wants to log in to the account.

### What is a Password Authentication System?

A password authentication system is a system that is used for the identification of a user. Think of it like a login screen that you see while logging in to your Facebook account. It asks for your email or a username and then it asks for your password. If you have entered the correct password then it verifies you as the real user.

Creating a logic-based password authentication system is also a popular question in the coding interviews. So, in this project, you will go through how to create a password authentication system using Python.

### Password Authentication using Python

To create a password authentication system using Python you have to follow the steps mentioned below:

1. Create a [dictionary](https://thecleverprogrammer.com/2020/12/31/python-dictionaries-tutorial/) of usernames with their passwords.
2. Then you have to ask for user input as the username by using the input function in Python.
3. Then you have to use the getpass module in Python to ask for user input as the password. Here we are using the getpass module instead of the input function to make sure that the user doesn’t get to see what he/she write in the password field.

### Output

```
Enter Your Username: john.doe
Enter your password: 
Enter Your Password Again: 
Enter Your Password Again: 
Verified
```

### Summary

So this is how we can authenticate the identity of a user by using the Python programming language. Now you can try the same logic with more usernames and other data structures also.
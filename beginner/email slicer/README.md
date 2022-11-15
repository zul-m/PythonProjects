## Email Slicer

An Email slicer is a very useful program for separating the username and domain name of an email address. In this project, I will explain how to write a program to create an Email Slicer with Python.

### Email Slicer with Python

To create an email slicer with Python, our task is to write a program that can retrieve the username and the domain name of the email. For example, look at the image below which shows the domain and username of “support@thecleverprogrammer.com”.

<p align="center">
 <img width="60%" src="./email.png" align="center" alt="Domain and username of support@thecleverprogrammer.com" />
</p>

So we need to divide the email into two strings using ‘@’ as the separator.

The code is very simple and easy to understand. We take user input and use the strip function at the same time to remove white space if any. Then we are finding the index of `@` symbol of the user input. Then we store the index into a variable known as `domain_name` to split the email into two parts; the user name and the domain. Finally, we are just formatting to print the output.

### Output

```
Enter your email: support@thecleverprogrammer.com
Your user name is 'support' and your domain is 'thecleverprogrammer.com'
```

### Summary

The code can be enhanced with more ideas depending on your needs. As a beginner, you must try these types of programs to improve your coding skills. In the long run, it will also help you build your algorithms and increase your ability to think logically.
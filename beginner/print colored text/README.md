## Print Colored Text

In Python the `Colorama` module allows us to easily create colored terminal text. In this project, I will take you through a tutorial on how to print Colored Text with Python by using the `Colorama` module in Python.

### What is Colorama in Python?

Using the `Colorama` module we can print colored text with Python. We can use it and call its built-in variables which are aliases for the desired `NSI codes. This makes our code more readable and works better with Windows command prompts after calling `colorama.init()` at the start of your script.

The `Colorama` module offers three main formatting options: Fore, Back, and Style. These allow us to change the foreground or background text color and style. The colors available for the foreground and background are black, red, green, yellow, blue, magenta, cyan, and white.

### Print Colored Text with Python

Traditionally, printing full-colour text to the terminal is accomplished by a series of escape characters on Linux or OS X systems. However, this will not work for Windows operating systems.

### Summary

It is also possible to change other text properties using ANSI escape characters. For example, if we wanted to make the text darker or lighter. You can learn more about this Python module from [here](https://pypi.org/project/colorama/).
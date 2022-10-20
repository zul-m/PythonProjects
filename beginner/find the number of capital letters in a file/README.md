## Count Capital Letters in a File

Counting the number of specific letters from a file is something that every coder should know. One of the most popular [coding interview questions](https://thecleverprogrammer.com/2021/03/11/the-most-popular-coding-interview-questions-using-python/) based on this logic is to count the number of capital letters from a file. So if you want to learn how to count the number of capital letters by reading any file, this project is for you.

### Python Program to Count Capital Letters in a File

Writing a program to count the number of capital letters in a file is an important coding question that you can get in any coding interview. You can get questions based on this logic in several ways. You will be given a text file, and you will be asked to read the file without using a Python library and print the number of capital or lowercase letters in the text file. So here’s how you can write a Python program to count capital letters in a text file.

In the code:
 1. I first opened a text file that was already saved on my computer
 2. Then I introduced a variable as count, which is used here to store the number of uppercase letters. 
 3. Initially, I declared its value to be 0, and in the next line, I am reading the text file
 4. Then I am using a for loop over the content of the text file and using the if statement inside the for loop which will keep adding 1 to the count variable until it keeps finding uppercase letters in the file using the `isupper()` function in Python.

Just like the above method, you can write a python program for counting small letters also by replacing the `isupper()` function with `islower()`.

### Output

```
21979
```

Now we replace the `isupper()` function with `islower()`.

```
652265
```
### Summary

So this is how you can find all capital letters in a file by using the Python programming language. It is an important coding question that you can get in any coding interview. You can get questions based on this logic in several ways.
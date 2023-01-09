## Language Detection

The task of language detection comes into use when you are working on a very large dataset that contains data in different languages. Suppose you want to create an even driven program where the final output depends on the language which the user provides as an input. So it is important to first detect the language of the text provided by the user before taking any action.

### Language Detection with Python

As an open-source programming language, Python provides libraries and packages for almost every possible task, as the Python programming community continues to contribute to Python with new libraries, packages, and modules. You can build your machine learning model for the language detection task, but for this project, I will be using the `langdetect` package in Python which can detect over 55 different languages within a few lines of code.

If you have never used this package before then you can easily install it by using the pip command.

```py
pip install langdetect
```

In the code, I started by importing the detect method from the `langdetect` package. Then, I am simply asking for user input where the user can enter text in any language. Then I am simply printing the language of the text entered by the user by detecting it using the detect method.

### Output

```
Enter any text in any language: สวัสดีฉันกําลังเรียนที่โรงแรมแคลิฟอร์เนีย
Language detected: th
```

### Summary

The output received is an abbreviated form of the language (`th` means Thai). So the user can enter text in whatever language the user likes, your program will detect that language but it will give the short form of that language as output.
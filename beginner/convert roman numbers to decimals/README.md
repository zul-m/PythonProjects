## Convert Roman Numbers to Decimals

One of the most favourite questions in a coding interview is to convert Roman numbers to decimals. In this project, I’ll walk you through how to write a Python program to convert Roman numbers to decimals.

### How To Convert Roman Numbers to Decimals?

Remember that the base numbers are not the numbers that are used by the Romans as they have count values such as `I: 1`, `V: 5`, `X: 10`, `C: 100`, `D: 500`, `M: 1000`, etc.

So we need to follow the above logic to write a program to convert roman numbers to decimals with Python. So let’s have a look at the process of converting roman numbers to decimals:
 1. Work your way through the string of Roman numerals from left to right, examining two adjacent characters at a time. If you want, you can also specify that the direction of loops, but it does not matter as long as the comparisons are implemented accordingly.
 2. If the value on the left is higher than the value on the right, then subtract the count at that position from the final value. Otherwise, just add it.
 3. Once the process is complete, the final value is the decimal value equivalent of the roman number.

### Python Program to Convert Roman Numbers to Decimals

Now let’s see how to write a program to convert Roman numbers to decimals. I’ll just follow the above explaination which is nothing more than an algorithm that defines the process of writing code to convert Roman numbers to decimals.

### Summary

I hope you liked this project on how to convert a roman number to a decimal with Python programming language. This is a solution to one of the most favourite questions of an interviewer in a coding interview.
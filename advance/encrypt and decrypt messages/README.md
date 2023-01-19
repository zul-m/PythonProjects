## Encrypt and Decrypt Messages

Cryptography means changing the text of a message so that people who don’t know your secret never understand your message.

### How to Encrypt and Decrypt using Python?

To encrypt and decrypt with Python, you need to create a program in which it will first ask you if you want to encrypt a message or decrypt it. Then the program should receive a message from the user.

If the user chooses to encrypt the message, the user’s message must be transformed into a secret code. But if the user chooses to decrypt the message, your program should be able to convert a secret code into a meaningful text.

For this task, you must write a program that rearranges the order of letters in user input so that it cannot be understood by anyone. This can be done by putting the letters in even and odd positions.

Then we have to swap the first two letters with the next two and so on. The code to convert encrypted text to decrypted text can be done by reversing the letters according to user input.

### Encrypt and Decrypt using Python

Now let’s see how to create a GUI application to encrypt and decrypt using Python. Here we need to write some code that uses an `infinite` loop that will keep asking the user if they want to encrypt or decrypt a message.

According to user input, we need to write an event program because the operation of the program depends on user input. Here we can use the dialogue box to get user input and the info box to show the encrypted and decrypted message to the user.

As stated before, I will be using an `infinite` loop, so the program will keep running until the user wants to encrypt and decrypt using Python. The program will end at the point where the user gives input other than “encrypt” and “decrypt”.

### Summary

Our code needs user input to be an even number of characters. The program first checks the number of characters entered by the user, if the character length is odd, the program will add `x` at the end to make the count even.
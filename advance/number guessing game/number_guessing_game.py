# To import random module.
import random

# To create a range of random numbers between 1-10.
n = random.randrange(1,100)

# To take a user input to enter a number.
guess = int(input("Enter any number: "))

while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
        break

print("you guessed it right!!")
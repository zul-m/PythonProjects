# Import the random module in Python.
import random
import string

print("Welcome to Password Picker")

# Create a list of adjectives for creating a password picker using Python.
adjectives = ['sleepy', 'slow', 'smelly', 'wet',
    'fat', 'red', 'orange', 'yellow', 'green',
    'blue', 'purple', 'fluffy', 'white', 'proud', 'brave'
]

# Create a list of nouns.
nouns = ['apple', 'dinosaur', 'ball', 'toaster',
    'goat', 'dragon', 'hammer', 'duck', 'panda'
]

while True:
    # Pick a random word from the lists.
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    # Select a random number between 0 and 99.
    # # Pick a random punctuation mark.
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    # Create a new password.
    password = adjective + noun + str(number) + special_char

    print("Your password is: %s" % password)

    # Generate another password if the user demands a different password.
    response = input("Would you like another password? Type Y or N >> ")
    if response == 'N':
        break
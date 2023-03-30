## Lives Game

In this game, you have to guess the secret word letter by letter. If you guessed a letter incorrectly, you will lose a life. As the title suggests, you need to choose the letters carefully as you will have a very limited number of lives.

### Lives Game with Python

To create a Lives game with Python, you need to write a program that shows you a mystery word with all the letters replaced by question marks. When you have correctly guessed the letter, your program should replace the question mark with this letter.

If you know what the word is, your program should also accept the full word as input rather than letter by letter only. The game should end when you have guessed the right word or you are out of life.

To create a Lives game with Python, you need to create two lists, one to store all the secret words and one to store the clues. Then using the random module, you have to make the random selection from the list of your secret words.

Then at the end, you need to run a `while` loop to check the player’s guesses and you also need to create a function at this point to update the hints.

### Output

```
['?', '?', '?', '?', '?']
Lives left: ❤❤❤
Guess a letter or the whole word: cat
Incorrect. You lose a life
['?', '?', '?', '?', '?']
Lives left: ❤❤
Guess a letter or the whole word: trousers
Incorrect. You lose a life
['?', '?', '?', '?', '?'] 
Lives left: ❤
Guess a letter or the whole word: house
Incorrect. You lose a life
You lost! The secret word was fairy
```

```
['?', '?', '?', '?', '?']
Lives left: ❤❤❤
Guess a letter or the whole word: pizza
Incorrect. You lose a life        
['?', '?', '?', '?', '?']
Lives left: ❤❤
Guess a letter or the whole word: fairy
You won! The secret word was fairy
```

### Summary

In the end, we need to check if the player has won on not. You can try this game and modify it according to your needs.

I hope you liked this project on how to create a game of life with the Python programming language.
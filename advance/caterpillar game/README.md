## Caterpillar Game

You must have played the caterpillar game on your cell phones when we are not introduced with smartphones. It’s a game about the hungry caterpillar that grows after every meal.

### How To Create a Caterpillar Game with Python?

To make a caterpillar game with python you need to develop a logic in which you will use the four arrow keys to move around the caterpillar to make it eat the leaf, every time it eats the leaf it will grow bigger and move around faster. You have to keep the caterpillar inside the widow otherwise the game will be over.

The more leaves the caterpillar eats, it will make the game difficult to play as the caterpillar will get bigger and move faster, which means you will have to play with the arrow keys faster.

To create this game using Python, I’m going to use the `turtle` module. Here I will be using two turtles; one to draw the caterpillar and one to draw the leaf. We need to program the two turtle objects so that one increases in size every time it comes in contact with the leaf and moves faster and the other appears in a random position every time the caterpillar eats leaf.

### Caterpillar Game with Python

To make the crawler game with Python, the biggest challenge is knowing how to move it around the screen. To move it around the screen, I’ll use an `infinite` loop. Each time the loop goes around, the caterpillar moves forward slightly. When the loop repeats quickly, these small movements will create the illusion that the caterpillar is crawling.

Let’s have a look at the process of creating the caterpillar game with Python before you start with the coding part:
 1. I will first start by setting the properties of leaf and the caterpillar.
 2. Then I will set the starting values like the speed and size of the caterpillar at the start of the game and the score of the game.
 3. Then I will program the caterpillar to move forward, here I will be using the if and else statements; to check if the caterpillar has made contact with the leaf or not.
 4. If the caterpillar has not made contact with the leaf we will check that whether it has left the screen or not, if it has left the screen we will stop the game and show the game over.
 5. If the caterpillar has now left the screen we will move the leaf in a now random position and increase the size of the caterpillar and increase the score. 
 6. And we will keep repeating this process.

### Summary

Run the game and you will see the output.
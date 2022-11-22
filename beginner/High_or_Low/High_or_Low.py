import random
n=random.randint(1,100)
chances_to_guess=3
guessed=False;
while chances_to_guess>0:
	guess=int(input())
	if(guess==n):
		print("You Won")
		guessed=True
		break
	elif guess<n:
		print("Too Low")
		chances_to_guess=chances_to_guess-1
	elif guess>n:
		print("Too High")
		chances_to_guess=chances_to_guess-1
if(guessed==False):
	print("You Lose")
	print("Number was: ",n)

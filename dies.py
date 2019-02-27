import random

while True:
	d = input("WELCOME TO SNAKE AND LADDER GAME!! Press R to roll ; E to exit from the game.")
	if d == 'R':
		print(random.randint(1,6))

	elif d == 'E':
		print("Thank u for playing,Bye!! play again")
		exit()

print("End!")
	

import random
l=["r","p","s"]
 
while True:
	l = input("Hallo, Enter R for Choosing rock, P for choosing paper, S for chhoosing seasor or Q to quit")

	c = random.choice(l)
	print("Computer has choosen :" ,c)

	if l == c:
		print("The game is tie!!")
	elif l == "R" and c == "P":
		print("Computer has won!!")
	elif l == "R" and C == "S":
		print("You has won!!")
	elif l == "P" and c == "R":
		print("You has won!!")
	elif l == "S" and c == "R":
		print("Computer has won!!")
	elif l == "P" and c == "S":
		print("You has won!!")
	elif l == "S" and c == "P":
		print("Computer has won!!")

elif l == "Q":
	print("Bye!!")
	exit()







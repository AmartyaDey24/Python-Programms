import random

p = 0
d = 0
snl={8:37,13:34,38:9,11:2,28:4,40:68,52:81,76:97,93:64,89:70}

def rolldice():
	return random.randint(1,6)

while True:
	r = input("Press R to roll, Q to quit :")

	if r == 'R':
		d = rolldice()
		print("You got:",d)
		
		if d == 6 or d == 1:
			p = d
			print("Congratulations, you are in the game.")
			print("You start on" ,p)
			break
		else:
			print("You need to get 6 or 1 to star. Try again !! ")
	elif r == 'Q':
		exit()


while True:

	r  = input("Press R to roll the dice, Q to quit :")

	if r == 'R':
		d = rolldice()
		print("You got" ,d)
		p = p + d

		if p == 100:
			print("GREAT, You won!!")
			exit()

		if p > 100:
			p = p-d
			print("Wait till you get", 100-p,"or less. ")

		print("Your new position is" ,p)

		if p in snl:
			if p < snl[p]:
				print("Wow, you go a ladder.")
			else:
				print("Opps!!, you got bitten by a snake.")

			p = snl[p]
			print("Move to." ,p)
	
	elif r == 'Q':
		print("Bye!!")
		exit()
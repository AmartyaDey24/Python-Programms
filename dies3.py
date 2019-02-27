for i in range(1,7):
	r = input("WELCOME TO SNAKE AND LADDER GAME, PRESS R TO ROLL, E TO EXIT: ")
	if r == 'R':
		if i ==1 or i == 3 or i == 4:
			print("YOU GOT", 6)

		elif i == 2 or i == 5:
			print("YOU GOT:", 2)

		else:
			print("YOU GOT:", 3)

	elif r == 'E'
		print("THANK U FOR PLAYING THE GAME!!")
		exit()
print("YEAH!!, U WON!!")
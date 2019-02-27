i=1
a=6
b=4

while True:
	d=input("WELCOME TO SNAKE AND LADDER GAME, PRESS R TO ROLL, E TO EXIT: ")
	if d == 'R':
		if(i<17):

			print(a)
			i=i+1
		else:
			print(b)
	elif d == 'E':
		print("THANK U FOR PLAYING THE GAME!!")
		exit()
print("END!!")


	
	
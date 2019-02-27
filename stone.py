
import random
dict={"R":"Rock","P":"paper","S":"Seasor","Q":"Quit"}

d=["R","P","S"]
	
cc = 0
uc = 0
while True:
	
	l = input("Hallo, Enter R for Choosing rock, P for choosing paper, S for choosing seasor  or Press Q to quit: ")
	print("You have choosen ",dict[l],"!!")

	if l == "Q":
		print("Bye!!")
		exit()

	


	
     
	c = random.choice(d)
	print("Computer has choosen :" ,c)


	if l == c:
		print("The game is tie!!")
		print("User Score: ",uc)
		print("Computer Score: ",cc)

	elif l == "R" and c == "P":
		print("Computer has won!!")
		cc=cc+1
		print("User Score: ",uc)
		print("Computer Score: ",cc)



	elif l == "R" and c == "S":
		print("You has won!!")
		uc=uc+1
		print("User Score: ",uc)
		print("Computer Score: ",cc)

	elif l == "P" and c == "R":
		print("You has won!!")
		uc=uc+1
		print("User Score: ",uc)
		print("Computer Score: ",cc)

	elif l == "S" and c == "R":
		print("Computer has won!!")
		cc=cc+1
		print("User Score: ",uc)
		print("Computer Score: ",cc)

	elif l == "P" and c == "S":
		print("You has won!!")
		uc=uc+1
		print("User Score: ",uc)
		print("Computer Score: ",cc)

	elif l == "S" and c == "P":
		print("Computer has won!!")
		cc=cc+1
		print("User Score: ",uc)
		print("Computer Score: ",cc)

	
	







try:
	a = int(input("Enter: "))
	if a<=5:
		raise NameError
	else:
		raise TypeError
	
		
except NameError:
	print("Opps!!Error............you have chosen  equal to or less than 5")
except TypeError:
	print("Error..........you have chosen more than 5")
else:
	print("NO error!!")

finally:
	("Execution Completed!!")

	
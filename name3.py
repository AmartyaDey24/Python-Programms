def func(n):
	if n < 0:
		print("Incorrect input")

	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return func(n-1) + func(n-2)

print(func(9))
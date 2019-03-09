t = [1,3,5,7]
s = 2 
def func(t,s):

	for i in t:
		s = s * i
		return s

print(func(t,s))
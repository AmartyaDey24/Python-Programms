t=[]
print("1.", t)

t=["a", "abc", 6,7.9]
print("2.", t)

print("3.",t[2])

for i in t:
	print("4.", i)


t.append(12)
print("5.", t)




if 7.9 in t:
	print("6.", "YES!!")
else:
	print("6.", "NO!!")



p=len(t)
print(p)

t[1] = 6
print("7.", t)

import random
p=random.randint(0,5)
print("8.", p)
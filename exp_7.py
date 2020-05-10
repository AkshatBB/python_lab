while True:
	A=int(input("Enter number"))
	for b in range(0,A):
		for a in range(0,b):
			if (a*a+b*b==A*A):
				print("a= ",a," b= ",b)
			if (a*a+b*b>A*A):
				break
	k=input("for countinuing further press 0, else press 1 ")
	if k=='1':
		break

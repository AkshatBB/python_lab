n=int(input("Enter number of test cases\n"))
for i in range(0,n):
	p=[]
	q=[]
	b=input()
	c=b.split()
	c=list(map(int,c))
	for i in range(2,c[0]+1): 
		p.append(i)
	for i in range(2,c[1]+1):
		q.append(i)
	for i in p:
		for j in p:
			if(i==j):
				continue
			elif(j%i==0):
				p.remove(j)

	for i in q:
		for j in q:
			if(i==j):
				continue
			elif(j%i==0):
				q.remove(j)

	for i in p:
		for j in q:
			if(i==j):
				q.remove(i)
	print(q)
	

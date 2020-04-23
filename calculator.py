from math import sin,cos,tan,log
result=0.0
#functions

def res(result):
    print('result= ',result)

def add(a,b):
    result=a+b
    return result

def sub(a,b):
    result=a-b
    return result

def mul(a,b):
    result=a*b
    return result

def div(a,b):
    result=a/b
    return result

def fact(a,b):
    result=1
    for i in range(1,int(a+1)):
        result=result*i
    print(int(a),"!",end=" ")
    res(result)
    result1=1
    for i in range(1,int(b+1)):
        result1=result1*i
    return(result1)
    
#main code:
while True:
    op=input('''Enter the operation to be performed \n \t '+'-Addition  \t \t'-'-Subtraction\n \t '*'-Multiplication \t '/'-Division
        'clr'-Clear \t \t'end'-End\n \t '!'-Factorial \t \t'^'-Power\n \t '%'-Modulus \t \t'r'-Root
        'sin'-sine  \t \t'cos'-cosine\n \t 'tan'-tangent \t \t'ln'-log\n''')
    print("operation:",op)

    if op=='clr':
        result=0.0
        res(result)
        continue

    elif op=='end':
        break

    a=float(input("Enter 1st number "))
    b=float(input("Enter 2nd number "))

    if op=='+':
        result=add(a,b)
        res(result)

    elif op=='-':
        result=sub(a,b)
        res(result)

    elif op=='*':
        result=mul(a,b)
        res(result)

    elif op=='/':
        result=div(a,b)
        res(result)

    elif op=='^':
        result=pow(a,b)
        res(result)

    elif op=='!':
        result=fact(a,b)
        print(int(b),"!",end=" ")
        res(result)

    elif op=='%':
        result=a%b
        print(a,"%",b,end=" ")
        res(result)

    elif op=='r':
        result=b**(1/a)
        print(int(a),"√",b,end=" ")
        res(result)

    elif op=='sin':
        result=sin(a*0.0174533)
        result1=sin(b*0.0174533)
        print("sin(",a,")",end=" ")
        res(result)
        print("sin(",b,")",end=" ")
        res(result1)
    
    elif op=='cos':
        result=cos(a*0.0174533)
        result1=cos(b*0.0174533)
        print("cos(",a,")",end=" ")
        res(result)
        print("cos(",b,")",end=" ")
        res(result1)
    
    elif op=='tan':
        result=tan(a*0.0174533)
        result1=tan(b*0.0174533)
        print("tan(",a,")",end=" ")
        res(result)
        print("tan(",b,")",end=" ")
        res(result1)
    
    elif op=='ln':
        result=log(a)
        result1=log(b)
        print("log(",a,")",end=" ")
        res(result)
        print("log(",b,")",end=" ")
        res(result1)

    else:
        print("Enter valid operation seeing the index")
        
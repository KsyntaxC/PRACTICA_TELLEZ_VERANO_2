'''
Dado un x>100, mostrar los dígitos repetidos:
Ejm: si x:47527734 --> mostrar: 4, 7
'''
x=int(input("Intro x: "))
while x<=100: x=int(input("Intro x: "))
while x>0:
    d=x%10; x=x//10; x1=x; c=0
    while x1>0:
        d1=x1%10; x1=x1//10
        if d1==d:
            c=c+1
    if c>=1:
        print(d, end=", ")
        nx=x; y=0; po=1
        while nx>0:
            dnx=nx%10; nx=nx//10
            if dnx!=d:
                y=dnx*po+y
                po=po*10
        x=y
'''
Dado un x>100, mostrar los dígitos repetidos:
Ejm: si x:47527734 --> mostrar: 4, 7
'''
N=int(input("Intro x: "))
while N<100: N=int(input("Intro x: "))
R=0
for i in range(0,10):
    temp=N
    while temp!=0:
        D=temp%10
        temp=temp//10
        if D==i:
            R=R+1
    if R>1:
        print(i,end=", ")
    R=0
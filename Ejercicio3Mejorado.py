'''
Dado un x>100, mostrar los dígitos repetidos:
Ejm: si x:47527734 --> mostrar: 4, 7
'''
x=int(input("Intro x: "))
while x<100: x=int(input("Intro x: "))
c=0
for i in range(0,10):
    xt=x
    while xt!=0:
        d=xt%10
        xt=xt//10
        if d==i:
            c=c+1
    if c>1:
        print(i,end=", ")
    c=0
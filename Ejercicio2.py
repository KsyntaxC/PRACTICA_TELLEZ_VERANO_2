'''
Dado un x>100, eliminar el digito más pequeño:
Ejm: si x=47527734 --> Mostrar 4757734
'''
x=int(input("Intro x: "))
while x<=100: x=int(input("Intro x: "))
x1=x; m=9; y=0; po=1
while x1>0:
    d=x1%10
    x1=x1//10
    if d<m:
        m=d
while x>0:
    d=x%10
    x=x//10
    if d!=m:
        y=d*po+y
        po=po*10
print(y)
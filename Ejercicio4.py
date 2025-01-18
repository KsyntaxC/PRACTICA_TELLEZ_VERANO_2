'''
Dado dos números con diferente cantidad de dígitos, intercalar sus dígitos.
Ejm: Si x=1234 y Y=56 --> Z=152634
'''
x=int(input("Intro x: "))
y=int(input("Intro y: "))
po=1; z=0
while x>0 or y>0:
    if x>0:
        dx=x%10
        x=x//10
        z=dx*po+z
        po=po*10
    if y>0:
        dy=y%10
        y=y//10
        z=dy*po+z
        po=po*10
print(z)
'''
Dado dos números con diferente cantidad de dígitos, intercalar sus dígitos.
Ejm: Si x=1234 y Y=56 --> Z=152634
'''
import math
x=int(input("Intro x: "))
y=int(input("Intro y: "))
z=0
cdx=int(math.log10(x))+1
cdy=int(math.log10(y))+1
while x>0 or y>0:
    if x>0:
        dx=int(x/10**(cdx-1))
        x=x%10**(cdx-1)
        cdx=cdx-1
        z=z*10+dx
    if y>0:
        dy=int(y/10**(cdy-1))
        y=y%10**(cdy-1)
        cdy=cdy-1
        z=z*10+dy
print(z)
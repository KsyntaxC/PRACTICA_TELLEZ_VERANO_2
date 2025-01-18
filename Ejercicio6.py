'''
Dados 3 números positivos, unir sus digitos en un nuevo número.
Ejm: Si x=123, y=654, z=54 --> w=12365454
'''
import math
x=int(input("Intro x: "))
y=int(input("Intro y: "))
z=int(input("Intro z: "))
while x<0 or y<0 or z<0:
    x=int(input("Intro x: "))
    y=int(input("Intro y: "))
    z=int(input("Intro z: "))
cdx=int(math.log10(x))+1
cdy=int(math.log10(y))+1
cdz=int(math.log10(z))+1
s=0
s=s*10**(cdx)+x
s=s*10**(cdy)+y
s=s*10**(cdz)+z
print(s)
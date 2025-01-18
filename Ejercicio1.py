'''
Dado un x>100, mostrar el primer y el ultimo digito.
Ejm: si x=47736 --> mostrar 4 y 6
'''
import math
x=int(input("Intro x: "))
while x<=100: x=int(input("Intro x: "))
cd=int(math.log10(x))+1
pd=int(x//(10**(cd-1)))
ud=x%10
print(pd, ud)
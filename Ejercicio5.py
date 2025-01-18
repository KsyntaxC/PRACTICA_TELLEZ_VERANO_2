'''
Dado un número positivo, mostrar el o los digitos centrales.
Ejm: si x=12345 -> mostrar 3, si x=123456 -> mostrar 34
'''
import math
x=int(input("Intro x: "))
cd=int(math.log10(x))+1
c=cd//2
if cd%2==1:
    dc=(x//10**c)%10
    print(dc)
else:
    xt=x//10**(c-1)
    dc1=xt%10
    dc2=(xt//10)%10
    print(dc2,dc1)
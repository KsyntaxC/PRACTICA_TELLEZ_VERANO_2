'''
Dado un lote de N números, eliminar el o los dígitos del medio
'''
import math
N=int(input("Intro N: "))
for i in range(1,N+1):
    x=int(input("Intro x: "))
    cd=int(math.log10(x))+1
    c=cd//2
    if cd%2==1:
        dc=(x//10**c)%10
    else:
        xt=x//10**(c-1)
        dc1=xt%10
        dc2=(xt//10)%10
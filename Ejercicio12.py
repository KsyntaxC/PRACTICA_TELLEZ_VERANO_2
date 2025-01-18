'''
Dados N casos de prueba: sumar los dígitos extremos de cada número
Ejm: Si N=4 y X=12,234,5687,43 → mostrar: 3,6,12,7
'''
import math
N=int(input("Intro N: "))
for i in range(1,N+1):
    x=int(input("Intro x: "))
    cd=int(math.log10(x))+1
    pd=x//10**(cd-1)
    ud=x%10
    s=pd+ud
    print(s)
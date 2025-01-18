'''
Dado un lote de N números, verificar si cada número es perfecto 
Un número es perfecto cuando la suma de sus divisores es igual al número
Ejm: si N=6, sus divisores son: 1,2,3 y la suma de sus divisores es 6
'''
N=int(input("Intro N: "))
for i in range (1,N+1):
    x=int(input("Intro x: "))
    s=0
    for j in range(1,x):
        if x%j==0:
            s=s+j
    if s==x:
        print("Es perfecto")
    else:
        print("No es perfecto")
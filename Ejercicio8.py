'''
Dado un lote de N números, mostrar los divisores de los pares
'''
N=int(input("Intro N: "))
for i in range (1,N+1):
    x=int(input("Intro x: "))
    if x%2==0:
        for j in range(1,x+1):
            if x%j==0:
                print(j)
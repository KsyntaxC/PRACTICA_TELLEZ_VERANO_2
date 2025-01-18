'''
Dado un lote de N números, mostrar los divisores de los pares
'''
N=int(input("Intro N: "))
for i in range (1,N+1):
    x=int(input("Intro x: "))
    if x%2==0:
        for i in range(1,x+1):
            if x%i==0:
                print(i)
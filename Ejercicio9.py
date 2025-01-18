'''
Dado un lote de N números, sumar y mostrar cada 2 consecutivos.
'''
N=int(input("Intro N: "))
s=0
for i in range(1,N+1):
    x=int(input("Intro x: "))
    s=s+x
    if i%2==0:
        print(s)
        s=0
    
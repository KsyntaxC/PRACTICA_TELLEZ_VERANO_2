'''
Dados N casos de prueba: mostrar el primer y último carácter en
mayúsculas de cada cadena ingresada. Ejemplo: Si N=4,
cad=”hola”,”juan”,”celeste”,”maría”-→ mostrar: H,A J,C C,E M,A
'''
N=int(input("Intro N: "))
for i in range(1,N+1):
    cad=input("Intro cad: ")
    if len(cad)>0:
        pc=cad[0].upper()
        uc=cad[len(cad)-1].upper()
    print(pc,",",uc)

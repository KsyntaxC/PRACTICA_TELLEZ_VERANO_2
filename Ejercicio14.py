'''
Dada una cadena C, sustituir los espacios por “$$$$$”
C=”Hola Mundo” → C1=”Hola$Mundo”
'''
cad=input("Intro cad: ")
t=len(cad)
y=""
for i in range(0,t):
    c=cad[i]
    if c!=" ":
        y=y+c
    else:
        y=y+"$"
print(y)
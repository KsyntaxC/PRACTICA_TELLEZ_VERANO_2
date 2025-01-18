'''
Dada una cadena C, eliminar las vocales
C=”Hola Mundo” → C1=”Hl Mnd”
'''
cad=input("Intro cad: ")
t=len(cad)
y=""
voc=["A","E","I","O","U","a","e","i","o","u"]
for i in range(0,t):
    c=cad[i]
    if c not in voc:
        y=y+c
print(y)
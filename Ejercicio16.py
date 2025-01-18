'''
Dada una cadena C, determinar cuántos signos de admiración tiene
'''
c=input("Introducir la Cadena: ")
t=len(c)
co=0
for i in range(0,t):
    if c[i]=="!":
        co=co+1
print("Tiene",co,"signos de admiración")
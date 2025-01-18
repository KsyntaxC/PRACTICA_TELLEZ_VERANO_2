'''
Dada una cadena C, contar cuantas veces aparece cada vocal
'''
c=input("Introduce una cadena: ")
t=len(c)
ca=0; ce=0; ci=0; co=0; cu=0
for i in range(0,t):
    if c[i]=="a" or c[i]=="A":
        ca=ca+1
    if c[i]=="e" or c[i]=="E":
        ce=ce+1
    if c[i]=="i" or c[i]=="I":
        ci=ci+1
    if c[i]=="o" or c[i]=="O":
        co=co+1
    if c[i]=="u" or c[i]=="U":
        cu=cu+1
print("La vocal a aparece",ca,"veces")
print("La vocal e aparece",ce,"veces")
print("La vocal i aparece",ci,"veces")
print("La vocal o aparece",co,"veces")
print("La vocal u aparece",cu,"veces")
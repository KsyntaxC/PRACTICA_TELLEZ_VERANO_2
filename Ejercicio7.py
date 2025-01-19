'''
Dado un número positivo, rotar cada 3 digitos.
Ejm: x=1234567 --> x=3216547
'''
import math
x=int(input("Intro x: "))
while x<0: x=int(input("Intro x: "))
cd=int(math.log10(x))+1
resultado = 0
while x > 0:
    if cd > 3:
        grupo = x // (10 ** (cd - 3))  # Extraer los primeros 3 dígitos
        x %= (10 ** (cd - 3))  # Eliminar los primeros 3 dígitos del número
        cd = int(math.log10(x)) + 1  # Actualizar la cantidad de dígitos
        # Rotar el grupo de 3 dígitos
        rotado = 0
        for i in range(3):
            rotado = rotado * 10 + grupo % 10
            grupo //= 10
        resultado = resultado * (10 ** 3) + rotado
    else:
        resultado = resultado * 10 + x
        x = 0  # Esto terminará el bucle sin necesidad de `break`

print(resultado)

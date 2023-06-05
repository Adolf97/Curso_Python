n1 = input("Ingresa primer número")
n2 = input("Ingresa segundo número")  # Para obtener datos del usuario

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
mult = n1 * n2
div = n1 / n2

mensaje = f"""
Para los números {n1} y {n2}:
El resultado de la suma es: {suma}.
El resultado de la resta es: {resta}.
El resultado de la multiplicación es: {mult}.
El resultado de la división es: {div}.
"""

print(mensaje)

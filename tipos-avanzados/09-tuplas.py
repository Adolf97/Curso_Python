# La única diferencia entre Tuplas y Listas, es que las Tuplas son inmutables
# Para iniciar una tupla, es con paréntesis

# numeros = (1, 2, 3) + (4, 5, 6)
# print(numeros)

nombres = ["Adolfo", "Carlos", "Gabriel",
           "Isaac", "Jorge", "Cristian", "Armando"]

nombresTupla = tuple(nombres)
print(nombresTupla)

menosNombres = nombresTupla[:4]
print(menosNombres)

primero, segundo, *otros = nombresTupla
print(primero, segundo, otros)

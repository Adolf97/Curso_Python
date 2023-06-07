# numeros = [2, 5, 12, 34, 9, 70]

# # numeros.sort(reverse=True)  # Sirve para ordenar la lista
# # A diferencia de sort(), sorted() entrega una nueva lista
# numeros2 = sorted(numeros)
# print(numeros)
# print(numeros2)

usuarios = [
    ["Adolfo", 4],
    ["Ernesto", 1],
    ["Héctor", 10]
]

# Las funciones lambda sirven cuando sólo vamos a llamar a una función una única vez
# Considerar que no es una buena práctica, tener todo el código lleno de funciones lambda
usuarios.sort(key=lambda el: el[1])
print(usuarios)

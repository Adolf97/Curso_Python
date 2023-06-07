# lista = [1, 2, 3, 4]
# # Nos sirve para desempaquetar los valores de una lista. También funciona para las tuplas

# lista2 = [5, 6]

# combinada = [*lista, *lista2]
# print(combinada)

punto1 = {"x": 19, "y": 45}
punto2 = {"y": 15}

# Los valores se asignan desde la derecha hacia la izquierda
nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)

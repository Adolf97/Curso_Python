numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# No podemos desempaquetar un sólo valor de una lista, tenemos que desempaquetar todos
# primero, segundo, tercero = numeros
# print(primero, segundo, tercero)

primero, *otros, ultimo = numeros
print(primero, otros, ultimo)

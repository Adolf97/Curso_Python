diccionario = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4
}

del diccionario['a']
print(diccionario)

valor = diccionario.pop('b')
print(valor)

llave = 'c'
valor2 = diccionario.pop(llave)
print(valor2)

print(diccionario)


diccionario['a'] = 1
diccionario['b'] = 2
print(diccionario)

diccionario.clear()
print(diccionario)
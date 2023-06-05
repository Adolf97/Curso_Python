diccionario = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4
}

valor = diccionario['b']
print(valor)

valor = diccionario.get('d')
print(valor)
valor = diccionario.get('r')
print(valor)
valor = diccionario.get('t', 'No existe :(')
print(valor)
valor = diccionario.get('c', 'No existe :(')
print(valor)


print("WACHA")
valor = diccionario.setdefault('e', 5)
print(valor)
print(diccionario)
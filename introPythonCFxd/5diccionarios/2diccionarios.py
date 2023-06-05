elementos = {}

elementos['nombre'] = 'Ernesto'
print(elementos)
print(len(elementos))


elementos[(1, 2, 3)] = 'La llave es una tupla'
print(elementos)
print(len(elementos))

#Si la llave no existe, la crea, si sí, la actualiza
elementos['nombre'] = 'Curso de Python en CódigoFacilito'
print(elementos)


elementos = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'a' : 4
}

#Aunque tenga llaves duplicadas, el diccionario sólo se quedará
#con una, y el valor será el último que se asignó
print(elementos)
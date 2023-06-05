#El equivalente a un json en Python es un diccionario

diccionario = {}
diccionario = dict()

diccionario = {
    'total' : 55
}

print(diccionario)

diccionario['cliente'] = 'Ernesto'
print(diccionario)

print(diccionario.keys())
print(diccionario.values())

for key, value in diccionario.items():
    print(key, value)


usuario = {
    'name' : 'Ernesto',
    'age' : 23,
    'major' : 'LSIA'
}

calificaciones = usuario.get('calificaciones', [])
if calificaciones:
    for calificacion in calificaciones:
        print(calificacion)
print(usuario)


usuario = {
    'name' : 'Ernesto',
    'age' : 23,
    'major' : 'LSIA',
    'calificaciones' : [8, 9, 7, 8]
}
calificaciones = usuario.get('calificaciones', [])
if calificaciones:
    for calificacion in calificaciones:
        print(calificacion)


###DICK COMPREHENSIOxd
print('DICTIONARY COMPREHENSION')
usuarios = ['Eduardo', 'Ernesto', 'Fernando', 'Uriel', 'Rafael']
diccionario_2 = { usuario : position + 1
                 for position, usuario in enumerate(usuarios)}

print(diccionario_2)
nombre = 'Ernesto'
apellido = 'Ramírez'

nombre_completo = nombre + apellido
print(nombre_completo)
nombre_completo = nombre + ' ' + apellido
print(nombre_completo)
nombre_completo = 'Sr ' + nombre + ' ' + apellido
print(nombre_completo)


print("WACHA: ")
nombre_completo = 'Sr %s %s.' %(nombre, apellido)
print(nombre_completo)


print("CON PLACEHOLDERS :O")
nombre_completo = 'Sr {} {} II.'.format(nombre, apellido)
print(nombre_completo)

print("CON PARÁMETROS (o algo asíxd)")
nombre_completo = 'Sr {apellido} {nombre} {puesto}'.format(
    nombre = nombre,
    apellido = apellido,
    puesto = 'II'
)
print(nombre_completo)
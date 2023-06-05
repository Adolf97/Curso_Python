calificacion = 8
color = None

if calificacion >= 7:
    color = 'verde'
else:
    color = 'rojo'

print(calificacion, color)


calificacion = 6
color = 'verde' if calificacion >= 7 else 'rojo'
print('Otro: ', calificacion, color)
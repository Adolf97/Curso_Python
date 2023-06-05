#Python asignará el primer valor verdadero con el que se tope

variable = 'Cody' or 'CódigoFacilito'
print(variable)


variable = '' or 'CódigoFacilito'
print(variable)


variable = '' or [] or 0 or True
print(variable)


print('Watch out, homeboy')
listado = []
nombre = 'Cody'

if listado:
    variable_2 = listado
else:
    variable_2 = nombre

print(variable_2)

variable_3 = listado or nombre
print('Variable 3: ', variable_3)
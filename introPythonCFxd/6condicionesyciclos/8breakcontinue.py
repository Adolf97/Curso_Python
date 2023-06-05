titulo_curso = 'Curso Profesional de Python'

for caracter in titulo_curso:
    print(caracter)


print('==============================')

for caracter in titulo_curso:
    if caracter == 'P':
        break
    print(caracter)


print('==============================')

for caracter in titulo_curso:
    if caracter == ' ':
        continue
    print(caracter)
print('********************')
for caracter in titulo_curso:
    if caracter == 'o':
        continue
    print(caracter)
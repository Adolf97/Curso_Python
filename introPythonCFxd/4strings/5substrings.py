titulo_curso = 'Curso Profesional de Python'

counter = titulo_curso.count('Python')
print(counter)


titulo_curso = 'Curso Profesional de Python, donde aprenderemos Python xd'
counter = titulo_curso.count('Python')
print(counter)


#Buskr algo que no exista
counter = titulo_curso.count('+')
print(counter)


#También se puede usar in
print('Python' in titulo_curso)
print('python' in titulo_curso)
print('python' in titulo_curso.lower())


print(titulo_curso.startswith('Curso'))
print(titulo_curso.startswith('Python xd'))

print(titulo_curso.endswith('Python xd'))
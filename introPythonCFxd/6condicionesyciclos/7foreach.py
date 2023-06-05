usuarios = ['usuario1', 'usuario2', 'usuario3', 'usuario4', 'usuario5']

for usuario in usuarios:
    print(usuario)


rango = range(10) #Empieza en 0 y termina en N-1 range(N)

for valor in rango:
    print(valor)
print('==============================')
for valor in range(10, 20):
    print(valor)
print('==============================')
for valor in range(20, 51, 2):
    print(valor)


numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for index,  number in enumerate(numeros):
    print(index, number)
#Vamos a cambiar el índice
#Ahora los índices empiezan en 11
for index,  number in enumerate(numeros, 11):
    print(index, number)
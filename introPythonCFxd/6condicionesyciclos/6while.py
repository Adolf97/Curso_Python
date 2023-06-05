#Se usa para cuando no sabemos el número de iteraciones

contador = 1
while contador <= 10:
    print(contador)
    contador += 1
'''Este ejemplo no está chido porque sabemos que son 10'''


numero = 1812
contador_digitos = 0
while numero >= 1:
    contador_digitos += 1
    numero /= 10

print('Tu número posee ', contador_digitos, ' digitos')


numero = 18120
contador_digitos = 0
while numero >= 1:
    contador_digitos += 1
    numero /= 10
else:
    print('Fin del ciclo')
    print('Tu número posee ', contador_digitos, ' digitos')
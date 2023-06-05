def suma(n1, n2):
    resultado = n1 + n2
    return resultado
#Puedes returnar el número de cosos (valores?) que quieras,
#pero no es muy recomendado returnar tantos
#con máximo 3 está muy bien el return
def resta(n1, n2):
    return 'La resta es = ', n1 - n2

n1 = int(input('Ingresa el primer número: '))
n2 = int(input('Ingresa el segundo número: '))

resultado = suma(n1, n2)
print('El resultado es = ', resultado)

mensaje, resultado2 = resta(n1, n2)
print(mensaje, resultado2)
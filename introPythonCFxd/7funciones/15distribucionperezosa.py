'''
    Ventajas de usar generadores:
    *la forma en la que iteramos cada uno de los objetos que el generador genera y retorna
    *con el lazy iterator conseguimos los valores que queremos 'on demand', por lo que, al sólo obtener los valores que necesitamos cuando lo necesitamos, no reservamos espacio de memoria que probablemente ni vayamos a usar.- Esto servirá mucho al trabajar con colecciones muy grandes
'''
def pares():
    for numero in range(0, 101, 2): #Lazy iterator
        #Una vez hayamos comenzado el generador, fácilmente podemos ir obteniendo cada uno de sus valores conforme lo vayamos necesitando
        yield numero


def pares2():
    for numero in range(0, 10, 2):
        yield numero

generador = pares()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

'''***Los podemos usar cuando trabajemos con colecciones grandes donde es muy probable que no necesitemos todos los registros de una bna, sino que los vayamos consumiendo conforme lo vayamos requiriendo***'''
#Si tratamos de obtener el siguiente elemento del generador, usando la función next, una vez que éste ya haya finalizado, es probable que nos dé error === 'StopIteration' - Lo podemos evitar con 'try' y 'except'

print('==============================')
print('OTRO EJEMPLO')
generador = pares2()
while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El generador finalizó')
        break
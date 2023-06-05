#A través de los decoradores seremos capaces de reducir líneas de código duplikdas, haremos nuestro código más legible, fácil de testear, fácil de mantener, y sobretodo, más Pyhtónicoxd
'''
    Un decorador no es más que una función que toma como input una función, y a su vez retorna otra función. Al implementar un decorador, estamos trabajando con al menos 3 funciones: input, output, principal

    a -> Función principal (decorador)
    b -> Función a decorar
    c -> Función decorada

    Generalmente haremos uso de los decoradores siempre que queramos extender funcionalidades a una función, ya sea porque no podamos modifikr la función, o porque no queremos hacerlo

    a(b) : c
'''

def funcion_a(funcion_b):

    def funcion_c():
        #pass
        '''Aquí se pueden poner tareas, incluso complejas'''
        print('***Antes del llamado')

        funcion_b() #Para decorar de forma correcta nuestra función
        
        '''Aquí también se pueden poner'''
        print('***Después del llamado')

    return funcion_c


#Para poder decorar la función
@funcion_a
def saludar():
    print('Hola, nos encontramos en una función')


#Al llamar a una función a decorar, no estamos ejecutando directamente la función a decorar, si no que estamos ejecutando la función que se nos retorna, en este caso la funcion_c, que no hace nada, por lo que no se muestra nada
saludar()

'''
    Sirve cuando queremos añadir funcionalidades sin tener que modifikr directamente la función
'''

@funcion_a
def suma():
    print(10 + 20)


suma()
'''Pueden haber decoradores para decoradores, decoradores para métodos, decoradores para clases, etc'''
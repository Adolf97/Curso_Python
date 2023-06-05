#Podemos testear funciones utilizando el docstring
#Podemos comprobar el funcionamiento haciendo uso únicamente de comentarios :o

def suma(num1, num2):
    """
    BREVE DESCRIPCIÓN
    *****************

    La función suma dos números enteros

    Argumentos:
    num1 (int)
    num2 (int)

    se retorna la suma de los 2 parámetros

    TODO: (lista )
        *


    Todo esto se almacena en el atributo __doc__
    Obejtos documentables


    ***PRUEBA***
    >>> suma(10, 20)
    30

    >>> suma(8, 5)
    13

    #>>> suma(8, 5)
    'mientras más me la mamas, más me crecexd'


    """
    return num1 + num2


def resta(num1, num2):
    """

    >>> resta(100, 50)
    50
    
    """
    return None


#Se prueba con python -m doctest [nombre del archivo]
#Si no se obtiene error, fue exitoso
#Hay que tratar de minimizar las pruebas, dejar sólo 2-3
#Doctest se encarga de probar todos los objetos documentables


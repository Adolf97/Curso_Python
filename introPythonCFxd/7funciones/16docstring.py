#Siempre es buena práctica documentar las funciones
'''Un Docstring no es más que un comentario que se colok en la primera línea de código de la función - Por convención, se usa triple-comillas-dobles'''

#__doc__ (módulos, clases, métodos, funciones)


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
    """
    return num1 + num2


#print(suma.__doc__)
print(help(suma))
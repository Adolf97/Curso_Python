'''
    Un generador es un tipo especial de función que retorna objetos que podemos iterar de manera sencilla sin que la función finalice
'''
#Se hará un generador que permita iterar todos los números pares que se encuentren entre 0 y 101
'''***Ésta no es***'''
def pares1():
    for numero in range(0, 101, 2):
        #print(numero)
        return numero #Esto la va a terminar en 0

    #Nada después de return se va a ejecutar, porque la función ya finalizó
    print('Este mensaje no se ve')


#A diferencia de return, que finaliza la función al retornar algo, con yield suspendemos de forma momentánea la ejecución para retornar un objeto, una vez que este objeto se yieldeó (retornó, pero le voy a poner así para no confundirmexd), la función se reanuda donde se detuvo
'''Ya es un generador :'v'''
def pares2():
    for numero in range(0, 101, 2): #Lazy iterator
        #Una vez hayamos comenzado el generador, fácilmente podemos ir obteniendo cada uno de sus valores conforme lo vayamos necesitando
        yield numero
        print('Esto va después de nuestro for de abajito')


print(pares1())
print(pares2()) #Esto imprime un obj de tipo generador

for par in pares2():
    print(par)
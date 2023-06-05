animal = 'León'


#La variable que tiene por valor León no está siendo modificada
#es por el scope, la que tiene Ballena sólo existe en la función
def imprimir_animal():
    animal = 'Ballena'
    print(animal)
    print(id(animal))


#Las variables globales se pueden modificar
#haciendo uso de global
def imprimir_otro_animal():
    global animal
    animal = 'Nutria'
    print(animal)
    print(id(animal))

imprimir_animal()
print(animal)
#También podemos diferenciar las variables por su id
print(id(animal))

print('==============================')
imprimir_otro_animal()
print(animal)
print(id(animal))
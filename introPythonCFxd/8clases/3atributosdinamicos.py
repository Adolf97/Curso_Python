'''
    Podemos añadir atributos de forma dinámica, los qales se almacenan en __dict__
'''

class Usuario:
    username = 'Username por default'
    email = ''


user1 = Usuario()
user2 = Usuario()

user1.username = 'Ernesto' #Añadimos el atributo al objeto

print(id(user1.username))
print(id(Usuario.username))

#Qando Python nota que asignamos un  valor a un atributo que no existe, se añade el atributo al objeto
#Si se modifik, no pasa nada, nomás se modifik y yaxd
user1.edad = 23


print(user1.__dict__)

print(user2.edad)
'''Los objetos pueden tener distintos atributos'''
#No es muy buena idea andar añadiendo atributos de manera dinámica a los objetos, se nos puede hacer un kgadero
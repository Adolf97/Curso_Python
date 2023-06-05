#De clase : los que pertenecen a la clase - Si los queremos usar, tenemos que hacer uso de la clase obligatoriamente
#De instancia : los que pertenecen a un objeto - Para usarlos tenemos que trabajar, obligatoriamente, con el objeto

class Usuario:
    username = 'Username por default'
    email = ''


#Usuario.username = 'Un usuario'
#Usuario.email = 'info@mail.com'


user1 = Usuario()
'''No debería de tener el atributo username, pero se le pueden agregar atributos en tiempo de ejecución'''
'''
*1.- Chekr si el atributo existe dentro del objeto
*2.- Chekr si el atributo existe dentro de la clase - Sólo lectura
*3.- Si queremos acceder a un atributo que no existe ni en el objeto ni en la clase, nos manda error
'''
print(id(user1.username))
print(id(Usuario.username))

#__dict__ - Contiene todos los atributos que posea nuestro objeto
print(user1.__dict__)
#***print(user1.edad) #Tira error
#Lo mejor es estandarizar los objetos
class Usuario:

    #Para que una función pueda ser considerada un método, se necesita un parámetro, que hará referencia al objeto per sé, aquél que llama al método
    '''Se puede poner el nombre que queramos, pero por conveniencia, se pone self, haciendo referencia a sí mismo'''
    def inicializar(self, username, edad):
        self.username = username
        self.edad = edad


user1 = Usuario()
user2 = Usuario()

user1.inicializar('ernesto', 23)
user2.inicializar('bololo', 20)

print(user1.__dict__)
print(user2.__dict__)
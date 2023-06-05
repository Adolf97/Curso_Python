#Para definir e inicializar atributos para un obj al momento de crearlo, usaremos el método __init__

class Usuario:
    
    #El método __init__ se llamará cuando estemos instanciando un objeto
    def __init__(self, username='', password=''):
        self.username = username
        self.password = password


user1 = Usuario('ernesto', '12345')
user2 = Usuario('bololog', '54321')
user3 = Usuario()

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
'''En Python, una clase puede heredad de múltiples clases'''

class Animal():
    def comer(self):
        print('El animal come uwu')
    
    def dormir(self):
        print('El animal duerme owo')


class Mascota(Animal):
    pass


class Felino:

    def cazar(self):
        print('El felino es violento iwi')

#Después del nombre de la clase se colokn paréntesis, y en los paréntesis se pone el nombre de la clase padre
class Perro(Mascota):
    pass

class Gato(Mascota, Felino):
    pass


wallabi = Perro()
wallabi.comer()
wallabi.dormir()

xander = Gato()
xander.comer()
xander.dormir()
xander.cazar()

#Las clases Padres iwal pueden convertirse en clases Hijas
#Entre más nivel jerárquico tenga una clase, más abstracta se volverá
#Y mientras menos nivel jerárquico, más concreta
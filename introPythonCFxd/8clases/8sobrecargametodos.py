'''
    La sobreescritura/sobrecarga de métodos consiste en que una clase hija puede modifikr el comportamiento de los métodos de la clase Padre con el fin de que estos se adecuen a las necesidades de la clase hija
'''
class SerVivo():
    
    def dormir(self):
        print('El ser duerme -o-')

class Animal(SerVivo):
    def comer(self):
        print('El animal come uwu')


class Mascota(Animal):
    
    def comer(self):
        print('La Mascota come uwu')


class Felino:

    def cazar(self):
        print('El felino es violento iwi')


class Gato(Mascota, Felino):
    
    def __init__(self, name):
        self.name = name
    

    def comer(self):
        print(f'{self.name}, come uwu')
    
    '''
    def dormir(self):
        print(f'{self.name}, duerme owo')
    '''


zuricj = Gato('Zuricj')

#Al momento de querer usar un método, Python busk en la clase inmediata del objeto, y luego va subiendo, buskndo en las clases de las que heredó - Busk de izquierda a derecha:
zuricj.comer()
zuricj.dormir()
'''Ejemplo con lo de zuricj: se va a clase Gato, no encuentra los métodos. Se va a clase Mascota, tampoco. Pasa a Felino, andan iwal. Sube otro nivel para llegar a Animal(), ahí está'''
#Pueden haber oksiones en que incluso después de haber sobreescrito los métodos de la clase padre tengamos la necesidad de ejecutarlos
'''
    Lo mejor que podemos hacer es usar la función super, que nos dará acceso a la clase padre inmediata para hacer uso de sus métodos
'''
class SerVivo():
    
    def dormir(self):
        print('El ser duerme -o-')

class Animal(SerVivo):
    def comer(self):
        print('El animal come uwu')


class Mascota(Animal):
    
    def comer(self):
        super().comer()
        print('La Mascota come uwu')


class Felino:

    def cazar(self):
        print('El felino es violento iwi')


class Gato(Mascota, Felino):
    
    def __init__(self, name):
        self.name = name
    

    def comer(self):
        super().comer()
        print(f'{self.name}, come uwu')
    
    '''
    def dormir(self):
        print(f'{self.name}, duerme owo')
    '''


zuricj = Gato('Zuricj')

zuricj.comer()
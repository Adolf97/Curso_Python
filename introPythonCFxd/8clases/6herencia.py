'''
    Una clase puede volverse clase padre una N cantidad de veces
'''

class Mascota:
    
    def comer(self):
        print('La mascota come uwu')
    
    def dormir(self):
        print('La mascota duerme owo')


#Después del nombre de la clase se colokn paréntesis, y en los paréntesis se pone el nombre de la clase padre
class Perro(Mascota):
    pass


wallabi = Perro()
wallabi.comer()
wallabi.dormir()
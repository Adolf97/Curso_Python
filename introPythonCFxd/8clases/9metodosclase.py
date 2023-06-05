'''
    Al iwal que con los atributos, a los métodos también los podemos clasificar en:
    *De instancia - Estos ya los hicimosxd
    *De Clase - Para estos oqpamos decoradores
'''

class Circulo:

    pi = 3.1415926

    #Si queremos representar a la clase per sé, usamos un parámetro al que llamaremos cls (por convención), para hacer referencia a la clase
    @classmethod #Esto se pone para que Python no lo confunda con un método de instancia,ya que cls es sólo por convención
    def area(cls, radio):
        return cls.pi * (radio ** 2)
    '''Para poder hacer uso de este método, será a través de la clase'''



resultado = Circulo.area(10)
print(resultado)
'''Podemos darnos qenta que es un método de clase ya que lo estamos utilizando directamente con la clase, sin la necesidad de crear un objeto'''
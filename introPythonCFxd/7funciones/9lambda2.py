#Las funciones Lambda (anónimas), son aquellas que
#son expresadas en una sola línea de código,
#además de no poseer nombre. Comúnmente realizan
#tareas muy pequeñas

#La función lambda va a retonar el resultado de dicha
#operación, por lo que no es necesario poner return
funcion_grados = lambda grados : grados * 1.8 + 32
'''lambda <parámetros> : <cuerpo de la función>'''

print(funcion_grados(20))


'''
Siempre que se crea una expresión lambda, debe poseer un cuerpo

sin_parametros = lambda : True
parametros_default = lambda p1=10, p2=20, p3=30 : p1 + p2 + p3

asterisco = lambda *args, **kwargs : len(args) + len(kwargs)

No importa que no regrese nada
'''
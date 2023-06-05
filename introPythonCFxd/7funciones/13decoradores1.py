'''
    ¿Qué pasa si la función a decorar recibe argumentos y parámetros y retorna algún tipo de valor? Deberemos adaptar nuestro decorador para trabajar con argumentos, parámetros y valores
'''

def funcion_a(funcion_b):

    #Se ponen * y **
    def funcion_c(*args, **kwargs):
        #pass
        '''Aquí se pueden poner tareas, incluso complejas'''
        print('***Antes del llamado')

        resultado = funcion_b(*args, **kwargs) #Para decorar de forma correcta nuestra función
        
        '''Aquí también se pueden poner'''
        print('***Después del llamado')

        #Hay que ponerle el return porque si no, pues la funcion_c no está regresando nada
        return resultado

    return funcion_c


@funcion_a
def suma(num1, num2):
    return num1 + num2


resultado = suma(15, 30)
print(resultado)

'''El decorador debe ser lo suficientemente flexible para poder recibir una n cantidad de argumentos y una n cantidad de parámetros, y en caso la función retorne algún tipo de valor, que la función decorada pueda retornar dicho valor'''
#La función c es la función que más tareas realizará
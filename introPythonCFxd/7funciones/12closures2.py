'''
    Un closure es una función que puede generar de forma dinámica otra función, y esta nueva función puede acceder a las variables lokles aún cuando la primera haya finalizado
'''

def saludar(username):
    mensaje_ = f'Hola, {username}' #Variable lokl

    def mostrar_mensaje():
        print(mensaje_)
    

    return mostrar_mensaje


username = 'Ernesto'
respuesta = saludar(username)

username = 'Héctor'

respuesta()
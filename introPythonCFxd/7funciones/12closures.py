def saludar():

    def mostrar_mensaje():
        print('Hola, nos encontramos en el curso de Python')
    

    #Sin juegoxd de paréntesis al final
    return mostrar_mensaje


respuesta = saludar()
print(respuesta)
print(type(respuesta))

#Si queremos llamar a una función a través de una variable,
#Colokmos la variable, paréntesis, y dentro de los paréntesis, todos los argumentos necesarios
respuesta()
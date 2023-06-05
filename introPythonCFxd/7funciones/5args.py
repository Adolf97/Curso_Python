def promedio(listado):
    return sum(listado) / len(listado)

#El * indica que todos los argumentos que entren a la
#Función formarán una tupla
#Todos los parámetros que posean asterisco
#deberán nombrarse args
def otro_promedio(*args):
    print(args)
    print(type(args))
    return sum(args) / len(args)


#Cuando nuestro programa contenga 2 o más funciones
#vamos a separarlas mediante 2 saltos, para leer mejor
def combinacion(p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)

calificaciones = (9, 8, 8, 7, 8)
resultado = promedio(calificaciones)
print(resultado)

print('==============================')
resultado = otro_promedio(9, 8, 8, 7, 8)
print(resultado)

print('******************************')
combinacion(10, 20, 1, 2, 3, 4, 5)
combinacion(10, 20, 6, 7, 8, 9, 10, p4=1000)
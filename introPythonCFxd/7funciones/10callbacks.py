#Funciones que son usadas como argumentos para otras funciones
promedio = lambda *args : sum(args) / len(args)

aprobatorio = lambda calificacion : calificacion >= 7

def es_aprobatorio(calificacion):
    return calificacion >= 90

def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    #Si se pasa args directamente, estamos pasando la tupla,
    #así que para desempaquetarla, hay que poner un * al inicio
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f'Felicidades, aprobaste con {promedio}')
    else:
        print(f'Reprobaste unu')


mostrar_mensaje(promedio, aprobatorio, 8, 8, 7, 9, 10, 8, 8, 6)
mostrar_mensaje(promedio, es_aprobatorio, 8, 8, 2, 9, 6, 8, 4)

'''
    Las callbacks sirven principalmente en programas que sean modularizables, donde se pueda reemplazar fácilmente una "pieza de software" por otra más
'''
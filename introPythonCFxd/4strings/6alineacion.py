#ljust -> Justifikr a la izquierda
#rjust -> a la derecha
#center -> centrar

mensaje = '¡Hola, Mundo!'

mensaje = mensaje.ljust(20)
print('.', mensaje, '.')


mensaje = '¡Hola, Mundo!'

mensaje = mensaje.rjust(20)
print('.', mensaje, '.')


mensaje = '¡Hola, Mundo!'

mensaje = mensaje.center(20)
print('.', mensaje, '.')
edad = 15
# Hay que tomar en cuenta el orden de cómo escribimos nuestras expresiones, ya que se evaluan de arriba hacia abajo
# y en caso de que una se evalúe como True, ahí termina de evaluar.
if edad > 54:
    print("Puede ver la película con descuento")
elif edad > 17:
    print("Puedes ver la película")
else:
    print("No puedes entrar")

print("Listo")

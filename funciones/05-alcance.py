saludo = "Hola Global"


def saludar():
    global saludo  # Esto es una mala práctica, no hay que hacerlo
    saludo = "Hola Mundo"
    print(saludo)


def saludarChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


print(saludo)
saludar()
saludarChanchito()
print(saludo)

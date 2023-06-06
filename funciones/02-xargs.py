def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5)
suma(3, 5, 12)
suma(9, -4, 24, 80)

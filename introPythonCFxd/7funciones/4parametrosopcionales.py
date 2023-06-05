def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2)

resultado = area_circulo(100)
print(resultado)

resultado = area_circulo(100, 3.1415926)
print(resultado)

resultado = area_circulo(pi=3.1415, radio=100)
print(resultado)
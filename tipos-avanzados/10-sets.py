# Set significa grupo o conjunto

primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)  # Para transformar una lista en un set
# segundo[0] # Nosotros no podemos acceder a los índices de un set, ya que no están ordenados
if 4 in segundo:  # Lo que si podemos hacer es ver si un valor se encuentra dentro del set
    print("Hola Mundo!")


# Al momento de imprimir, Python se encargará de no mostrar los elementos repetidos

# Este operador (unión) une los sets, sin repetir ningún valor
print(primer | segundo)

# Este operador (intersección) nos devuelve los valores que se encuentran en ambos sets
print(primer & segundo)

# Este operador (diferencia) se encarga de mostrarnos únicamente los valores del set de la izquierda,
# pero quitando los valores que también se encuentran en el set de la derecha
print(primer - segundo)

# Este operador (diferencia simétrica) nos devuelve los valores que no se repitan entre los sets
print(primer ^ segundo)

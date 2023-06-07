# # Para poder crear un diccionario, debemos abrirlo con paréntesis de llaves
# # Sólo aceptan strings como la llave, pero el valor de ésta sí puede ser cualquier tipo de archivo
# punto = {"x": 25, "y": 50}
# print(punto)
# print(punto["x"])
# print(punto["y"])

# punto["z"] = 45
# print(punto)

# # Con .get() podemos ver si nuestro diccionario contiene cierta llave.
# # En caso de que no exista, nos devolverá None,
# # o podemos darle un valor por defecto, escribiéndolo a la derecha
# print(punto.get("lala", 97))

# del punto["x"]
# del (punto["y"])
# print(punto)

# punto["x"] = 23
# for valor in punto:
#     print(valor, punto[valor])

# # Cuando iteramos un diccionario, con el método items(), esto nos devuelve tuplas
# for valor in punto.items():
#     print(valor)

# for llave, valor in punto.items():
#     print(llave, valor)


usuarios = [
    {
        "id": 1,
        "nombre": "Chanchito"
    },
    {
        "id": 2,
        "nombre": "Feliz"
    },
    {
        "id": 3,
        "nombre": "Adolfo"
    },
    {
        "id": 4,
        "nombre": "Felipe"
    }
]

for usuario in usuarios:
    print(usuario["nombre"])

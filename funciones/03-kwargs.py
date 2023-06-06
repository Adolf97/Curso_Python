def get_product(**datos):
    print(datos["id"], datos["name"])


# cuando usamos kwargs, al momento de llamar a la función, debemos poner el nombre del parámetro y su respectivo argumento
get_product(id="23",
            name="iPhone",
            desc="iPhone 12, 128gb, 8gb")

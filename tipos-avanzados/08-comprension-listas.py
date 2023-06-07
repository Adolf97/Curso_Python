usuarios = [
    ["Adolfo", 4],
    ["Ernesto", 1],
    ["Héctor", 10]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# Para transformar --> En JS es .map()
# nombres = [usuario[0] for usuario in usuarios]

# Para filtrar --> En JS es .filter()
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# Para filtrar y transformar al mismo tiempo
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

nombres = list(map(lambda usuario: usuario[0], usuarios))
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)

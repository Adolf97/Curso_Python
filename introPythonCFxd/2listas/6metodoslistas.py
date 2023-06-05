lista = [8, 90, 15, 34, 27, 33, 420, 69, 2]

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

print('Mínimo: ',min(lista), 'Máximo: ',max(lista))

print(10 in lista)
print(15 in lista)

print(34 not in lista)
print(23 not in lista)
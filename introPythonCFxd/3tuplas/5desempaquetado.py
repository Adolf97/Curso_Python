numeros = (1, 2, 3, 4, 5)
uno, dos, tres, cuatro, cinco = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)


numeros = (1, 2, 3, 4, 5, 6)
uno, dos, tres, cuatro, *restantes = numeros
#El asterisco denota listas

print(uno)
print(dos)
print(tres)
print(cuatro)
print(restantes)

numeros = (1, 2, 3, 4, 5, 6)
uno, dos, tres, cuatro, *_ = numeros
#Se coloca el guión bajo para omitir los demás valores

print(uno)
print(dos)
print(tres)
print(cuatro)

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, dos, tres, cuatro, *_, nueve, diez = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(nueve)
print(diez)

uno, dos, tres, cuatro, *restantes, nueve, diez = numeros
print(restantes)


numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, _, tres, cuatro, *_, nueve, diez = numeros
print(uno)
print(tres)
print(cuatro)
print(nueve)
print(diez)
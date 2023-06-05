'''
    *Nos permiten comparar valores booleanos
    OPERADORES
    and
    or
    not
'''

resultado1 = True and True
resultado2 = True and False
resultado3 = False and False
print(resultado1, "-", resultado2, "-", resultado3)

resultado1 = True or True
resultado2 = True or False
resultado3 = False or False
print(resultado1, "-", resultado2, "-", resultado3)

resultado1 = not True
resultado2 = not False
print(resultado1, "-", resultado2)

print("Combinarxd")
print(True and (False or 10 > 2))
print(True and (False or not 10 > 2))
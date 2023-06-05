def funcion_principal():
    a = 'a'
    b = 'b'

    def funcion_anidada():
        c = 'c'

        a = 'primer cambio de valor'
        print(a)
        print(id(a))

        nonlocal b
        b = 'segundo cambio de valor'
        print(b)
        print(id(b))

    
    funcion_anidada()

    print(f'A de funcion_principal = {a}')
    print(f'Id de A de funcion_principal = {id(a)}')
    print(f'B de funcion_principal = {b}')
    print(f'Id de B de funcion_principal = {id(b)}')


funcion_principal()


'''
    Si quisiéramos modifikr una variable lokl que se encuentre en un scope superior, hacemos uso de la palabra reservada:
    nonlocal

    Las variables pueden ser utilizadas en el bloque que fueron creadas y en subbloques (anidados). No pueden ser usadas afuera del bloque, ya que una vez que el bloque finaliza, se destruyen
'''
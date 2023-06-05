#Usar ** hará que no trabajemos con tuplas
#sino con diccionarios
def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))


def combinacion(*args, **kwargs):
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))


usuarios(ernest=[8,7,9,8], ernesto=[7,6,7,7])

combinacion(1, 2, 3, 4, 5, cody=True, curso='Python')
lenguajes = 'Python Ruby Java C# C++'

lista_lenguajes = lenguajes.split()
#Por default lo divide por espacios
print(lista_lenguajes)


lenguajes = 'Python-Ruby-Java-C#-C++'
lista_lenguajes = lenguajes.split()
print(lista_lenguajes)
lista_lenguajes = lenguajes.split('-')
print(lista_lenguajes)


print('CHEK')
lenguajes = 'Python-Ruby-Java-C#-C++'
lista_lenguajes = lenguajes.split('-', 2)
print(lista_lenguajes)


lista_lenguajes = ['Python', 'Java', 'JavaScript', 'C++']
string_lenguajes = ' '.join(lista_lenguajes)
print(string_lenguajes)
string_lenguajes = '*||*'.join(lista_lenguajes)
print(string_lenguajes)
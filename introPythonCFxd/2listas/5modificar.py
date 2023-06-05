lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
lista_cursos.append('MongoDB')
print(lista_cursos)

lista_cursos.append('C#')
print(lista_cursos)

lista_cursos.append('JavaScript')
print(lista_cursos)

lista_cursos.insert(2, 'C++')
print(lista_cursos)


lista_cursos_2 = ['C', 'Docker', 'Rails']
lista_cursos.extend(lista_cursos_2)
print("Nueva Lista")
print(lista_cursos)

lista_cursos.remove('Rails')
print(lista_cursos)

del lista_cursos[8]
print("Última Lista")
print(lista_cursos)


lista_cursos.clear()
print('Lista: ',lista_cursos, 'Tamaño: ',len(lista_cursos))
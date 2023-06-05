mensaje = """
Bienvenidos a la calculadora.
Para salir escribe Salir
Las operaciones son suma, multi, div y resta
"""

print(mensaje)

# num1 = ""
# while num1.lower() != "salir":
#     num1 = input("Ingresa número: ")
#     if num1.lower() == "salir":
#         break
#     op = input("Ingresa operación: ")
#     num2 = input("Ingresa siguiente número: ")

#     if op.lower() == "suma":
#         op = int(num1) + int(num2)
#         print(f"El resultado es: {op}")
#     elif op.lower() == "multi":
#         op = int(num1) * int(num2)
#         print(f"El resultado es: {op}")
#     elif op.lower() == "div":
#         op = int(num1) / int(num2)
#         print(f"El resultado es: {op}")
#     elif op.lower() == "resta":
#         op = int(num1) - int(num2)
#         print(f"El resultado es: {op}")
#     else:
#         print("Operación inválida")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente número: ")
    if op.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no válida")
        break

    print(f"El resultado es: {resultado}")

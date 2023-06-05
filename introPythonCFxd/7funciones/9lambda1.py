def centigrados_a_fahrenheit(grados):
    return grados * 1.8 + 32

print(centigrados_a_fahrenheit(10))
print(centigrados_a_fahrenheit(20))

#No poner los paréntesis, porque si se ponen
#nos va a dar lo que resulte de la función,
#y no la función como tal
mi_funcion = centigrados_a_fahrenheit
print(type(mi_funcion))

print(mi_funcion(16))
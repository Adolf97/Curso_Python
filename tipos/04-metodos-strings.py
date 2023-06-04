animal = "  chanCHito feLiz  "
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize()) # Se pueden encadenar métodos
print(animal.title())
print(animal.strip()) # Para quitar los espacios de ambos lados
print(animal.lstrip())
print(animal.rstrip())
print(animal.find("cH")) # Devuelve el índice donde se encuentra. Si devuelve -1 quiere decir que no lo encontró
print(animal.replace("nCH", "j"))
print("nCH" in animal) # Devuelve un boolean
print("nCH" not in animal)

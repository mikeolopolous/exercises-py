lista_chars = ["m", "a", "r", "j", "b", "g", "i", "s", "f"]
print(lista_chars)

eliminar = input("Introduce el item de la lista a eliminar: ").lower()

for e in lista_chars:
    if e == eliminar:
        lista_chars.remove(e)

print("Nueva lista: ", lista_chars)
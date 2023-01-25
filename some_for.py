texto = input("Ingresa una frase: ")
letra = input("Ingresa la letra a omitir: ")

texto = texto.lower()
letra = letra.lower()

for c in texto:
    if c == letra:
        continue

    print(c, end = "")

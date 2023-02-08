text = input("Ingresa una frase cualquiera: ").lower()
letters = set()

for c in text:
    if c != " ":
        letters.add(c)

print(letters)
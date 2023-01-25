frase = input("Ingresa una frase: ")
frase = frase.lower()

vocales = 0
i = 0
while i < len(frase):
    if frase[i] in "aeiou":
        vocales += 1
    i += 1

print("En total hay {} vocales".format(vocales))
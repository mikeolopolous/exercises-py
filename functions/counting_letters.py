def counter(frase, letra):
    frase = frase.lower()
    count = frase.count(letra)
    return count

frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

print(counter(frase, letra))
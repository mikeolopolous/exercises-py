frase = "El camino está cerrado pero seguro que podemos encontrar una alternativa"
print("Este es el string original: {}".format(frase))

palabra = input("Ingresa la palabra que deseas eliminar:\n")
print("Palabra: {}".format(palabra))

idx = frase.find(palabra)
substring = frase[:idx] + frase[(idx + len(palabra) + 1):]

print(substring)

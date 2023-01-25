texto = input("Ingresa un texto cualquiera: ")
texto_inv = ""

for letra in texto:
    texto_inv = letra + texto_inv
    
print(texto_inv)
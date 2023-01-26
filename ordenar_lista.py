print("Introduce 10 números: ")

lista_numeros = []

for i in range(10):
    n = int(input())
    lista_numeros.append(n)

print("¿En qué orden desear ordenarla?\nSelecciona una opción...")
print("1. Ascendente\n2. Descendente")
orden = int(input())

if orden == 1:
    lista_numeros.sort()
else:
    lista_numeros.sort(reverse=True)

print(lista_numeros)

limite = int(input("Ingresa el límite de la serie: "))

anterior = 1
actual = 1
idx = 3

print(f"{anterior}")

while actual <= limite:
    print(f"{actual}")

    temp = actual
    actual += anterior
    anterior = temp

    idx += 1
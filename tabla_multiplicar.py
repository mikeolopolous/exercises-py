numero = int(input("¿De qué número quieres la tabla? "))

for i in range(1, 11):
    print("{} x {} = {}".format(numero, i, numero * i))

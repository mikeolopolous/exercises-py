numero = float(input("Ingresa un número: "))

suma = 0
while numero != 0:
    suma += numero
    numero = float(input("Ingresa un número"))
else:
    print("La suma de todos los números es {}".format(suma))
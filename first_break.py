a = int(input("Introduce el extremo izquierdo del intervalo: "))
b = int(input("Introduce el extremo derecho del intervalo: "))

i = a
while i <= b:
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        print(i)
        break
    
    i += 1

if i == b + 1:
    print("No hay números enteros divisibles dentro del intervalo dado")
print("== Ecuaciones de PRIMER GRADO ==\n")
print("== Ax + B = 0 ==\n")

a = float(input("Ingresa valor de A: "))
b = float(input("Ingresa valor de B: "))

if a != 0:
    solucion = - b / a
    print(f"X= {solucion}")
else:
    print("Debes ingresar un valor diferente a '0'")

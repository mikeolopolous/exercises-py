year = int(input("Ingresa el año: "))

if year % 4 == 0:
    if year % 100:
        if year % 400:
            print(f"El año {year} es bisiesto")
        else: print(f"El año {year} no es bisiesto")
    else: print(f"El año {year} es bisiesto")
else: print(f"El año {year} no es bisiesto")
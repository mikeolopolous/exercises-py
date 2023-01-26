import numpy as np

rows = int(input("Introduce el número de filas: "))
columns = int(input("Introduce el número de columnas: "))

m = np.empty((rows, columns))

for row in range(rows):
    for column in range(columns):
        n = float(input())
        m[row][column] = n

print(m)
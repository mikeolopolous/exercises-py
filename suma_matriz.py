import numpy as np

rows_a = int(input("Introduce número de filas para Matriz A: "))
columns_a = int(input("Introduce número de columnas para Matriz A: "))

matriz_a = np.empty((rows_a, columns_a))
matriz_b = np.empty_like(matriz_a)

print("\n=== Matriz A ===")
for row in range(rows_a):
    for column in range(columns_a):
        matriz_a[row][column] = float(input())

print("\n=== Matriz B ===")
for row in range(rows_a):
    for column in range(columns_a):
        matriz_b[row][column] = float(input())

matriz_c = matriz_a + matriz_b

print("\n=== Resultado ===\n", matriz_c)
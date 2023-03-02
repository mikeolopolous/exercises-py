celsius = [0, 72, 89, 56, 44, 86, 74]

fahrenheit = list(map(lambda grade: grade * 1.8 + 32, celsius))

print(fahrenheit)
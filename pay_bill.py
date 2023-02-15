from random import choice

number_of_persons = int(input("Introduce el número de personas: "))
str_names = input("Introduce los nombres de las personas separados por comas: ")
names = str_names.split(", ")

loser = choice(names)

print(f"{loser} es quien debe pagar!")
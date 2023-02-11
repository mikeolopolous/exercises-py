frase = input("Introduce una frase: ").lower()
vocales = "aeiou"
total_vocales = 0
total_consonantes = 0
blank = " "
total_espacios = 0

for i in frase:
    if i in vocales:
        total_vocales += 1
    elif i.isalpha:
        total_consonantes += 1
    elif i == " ":
        total_espacios += 1

my_list = [
    ("vocales", total_vocales),
    ("consonantes", total_consonantes),
    ("espacios", total_espacios)
]

print(my_list)
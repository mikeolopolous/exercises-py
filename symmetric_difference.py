a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))

if b < a or d < c:
    print("No has proporcionado dos intervalos")
else:
    ab = set(range(a, b + 1))
    cd = set(range(c, d + 1))

    print(ab.symmetric_difference(cd))
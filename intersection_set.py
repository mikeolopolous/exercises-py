word1 = input("Palabra 1: ").lower()
word2 = input("Palabra 2: ").lower()

letters1 = set()
letters2 = set()

for c in word1:
    letters1.add(c)

for c in word2:
    letters2.add(c)

intersect = letters1.intersection(letters2)
print(intersect)
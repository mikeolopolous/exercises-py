import random

random_number = random.randint(0, 1)

if random_number == 1:
    coin = "heads"
else:
    coin = "tails"

print(f"The coin has {coin}")
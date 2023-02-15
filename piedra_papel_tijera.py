import random

piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [piedra, papel, tijera]

eleccion_jugador = int(input("Elige 0 para piedra, 1 para papel o 2 para tijera:\n"))

if eleccion_jugador >= 3 or eleccion_jugador < 0:
    print("Has ingresado un valor no permitido.")
else:
    print(images[eleccion_jugador])

    npc = random.randint(0, 2)
    print(f"El PC eligió\n{images[npc]}")

    if eleccion_jugador == 0 and npc == 2:
        print("Has ganado!")
    elif npc == 0 and eleccion_jugador == 2:
        print("Has perdido!")
    elif npc > eleccion_jugador:
        print("Has perdido!")
    elif eleccion_jugador > npc:
        print("Has ganado!")
    elif npc == eleccion_jugador:
        print("Es un empate!")
        
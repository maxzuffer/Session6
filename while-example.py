# you have 3 lives. I roll the dice: If I roll 6 you win, if not you loose 1 life.

from random import randint
# randint = random in

lives = 3
while lives > 0:
    roll = randint(1,6)
    if roll == 6:
        print("You won")
        break
    else:
        lives -= 1
        print(f"You loose 1 life, you have {lives}")
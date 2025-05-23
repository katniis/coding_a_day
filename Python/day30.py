# 30. Create a function roll() that generates 2 numbers between 1 to 6
from random import randint

def rolldice():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1, dice2

result = rolldice()

print(f"Dice 1: {result[0]}")
print(f"Dice 2: {result[1]}")

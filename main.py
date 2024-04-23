from random import randint

lotto = []
guess = []
guessed_numbers = 0

for i in range(6):
    x = randint(1, 49)
    if x not in lotto:
        lotto.append(x)


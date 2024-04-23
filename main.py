from random import randint

lotto = []
guess = []
guessed_numbers = 0

for i in range(6):
    x = randint(1, 49)
    if x not in lotto:
        lotto.append(x)

while len(guess) < 6:
    try:
        user_number = int(input("Enter 6 correct numbers from 1 to 49 to win: "))
        if user_number > 49:
            print("The number is too big!")
        elif user_number < 1:
            print("The number is too small!")
        elif user_number in guess:
            print("You have already picked that number!")
        else:
            guess.append(user_number)
    except ValueError:
        print("Please enter only numbers!")

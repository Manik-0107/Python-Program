import random

while True:
    n = int(input("\nPlease enter any Guess number between 1-5: "))
    num = random.randint(1, 5)

    if n==num:
        print("You WON")
        break
    else:
        print("You lost")
        print(f"The number was: {num}\n")
        continue




"""
Please enter any Guess number between 1-5: 3
You lost
The number was: 4


Please enter any Guess number between 1-5: 4
You WON

"""

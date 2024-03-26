import random
import sys

while True:
    try:
        n = int(input("Level: "))
        if n < 1:
            continue
        else:
            break

    except ValueError:
        continue
    else:
        break

range = random.randint(1,n)


while True:
    try:
        guess = int(input("Guess: "))

        if guess < range:
            print("Too small!")
        elif guess > range:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
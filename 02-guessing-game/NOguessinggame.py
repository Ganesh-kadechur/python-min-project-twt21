import random

top = input("type a number")

if top.isdigit():
    top = int(top)
    if top <= 0:
        print("please enter a number greater than 0")
        quit()
else:
    print("try  digit greater than 0  next time")
    quit()

random_number  = random.randrange(0,top)

guesses = 0

while True:
    guesses += 1
    guess = input("make a guess;")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("please enter a number greater than 0")
        continue

    if guess == random_number:
        print("right")
        break
    elif guess > random_number:
         print("you were above the number")
    else:
        print("you were below the number")


print("you got it in",guesses,"guesses")
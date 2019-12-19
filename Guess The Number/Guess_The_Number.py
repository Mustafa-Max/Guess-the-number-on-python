import random

hidden = random.randrange(0, 21)

guess = int(input("What number will you guess ? "))

if guess == hidden:
    print("Hit!")
elif guess < hidden:
   print("Your guess is too low")
else:
    print("Your guess is high")

print(hidden,"Don't give up")
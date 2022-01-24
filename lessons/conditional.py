"""An Example of conditional(if else) statements"""

SECRET: int = 3
#All Caps because its a constant
print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You got it right")
else:
    print("You guessed incorrectly")

print("Game over.")
"""EX02 - One-Shot Wordle- Loops!."""
__author__ = "730366585"
from operator import index


secret_word = "python"
secret_length = str(len(secret_word))
white_box = "\U00002B1C"
green_box = "\U0001F7E9"
yellow_box = "\U0001F7E8"
i = 0
boxes = ""

guess = input("What is your " + secret_length + "-letter guess?")

while len(guess) != len(secret_word):
    guess = input("That was not "+ secret_length+  " letters! Try again:")

while i != len(secret_word):
    if secret_word[i] == guess[i]:
      boxes = boxes + green_box+ " "
    else: 
        if guess[i] in secret_word: 
            boxes = boxes + yellow_box+ " "
        else:
            boxes = boxes + white_box+ " "
    i=i+1
print(boxes)
if secret_word == guess:
    print ("Woo! You got it!")
else:
    print ("Not quite. Play again soon!")
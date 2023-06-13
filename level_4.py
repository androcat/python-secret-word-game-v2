# Level Four
# Time for consequences! Add the "Hangman" feature to your game: after a certain number of tries, 
# you lose the game and have to start over.

import random

easy = ["hi", "boom", "yellow", "no", ]
medium = ["kittens", "babies", "puppies", "happy", "nothing", ]
hard = ["effervescent", "escalation"]
extreme = ["supercalifragilisticexpialidocious"]

tries = 6

selection = input("Please select the difficulty (easy/medium/hard/extreme): ")
if selection == "easy":
    secret_word_list = easy
elif selection == "medium":
    secret_word_list = medium
elif selection == "hard":
    secret_word_list = hard
elif selection == "extreme":
    secret_word_list = extreme
print("You can guess wrong",tries,"times")

secret_word = secret_word_list[random.randint(0, len(secret_word_list)-1)]
secret_word_list = list(secret_word)
secret_word_set = set(secret_word_list)
guess_list = []
is_word_guessed = False

while tries > 0:
    guess_letter = input("Guess a letter: ")
    tries -= 1
    if guess_letter in secret_word:
        guess_list.append(guess_letter)
        print("Correct!", guess_letter,"is in the word")
    if guess_letter not in secret_word:
        print("X Try again X")
    if sorted(secret_word_set) == sorted(guess_list):
        print("You win ! The correct word is",secret_word)
        break
    
if tries == 0 and sorted(secret_word_set) != sorted(guess_list):
    print("You lose :^( The correct word was:",secret_word)
# Level Three
# Let's make this more personal. In level three, separate your word choices into 
# "easy", "medium", and "hard". Allow the player to select a difficulty level & select their word 
# to guess from the corresponding data structure. _Hint: you might classify difficulty length of words, 
# since there's more to guess.

import random

easy = ["hi", "boom", "yellow", "no", ]
medium = ["kittens", "babies", "puppies", "happy", "nothing", ]
hard = ["effervescent", "escalation"]
extreme = ["supercalifragilisticexpialidocious"]

selection = input("Please select the difficulty (easy/medium/hard/extreme): ")
if selection == "easy":
    secret_word_list = easy
elif selection == "medium":
    secret_word_list = medium
elif selection == "hard":
    secret_word_list = hard
elif selection == "extreme":
    secret_word_list = extreme

secret_word = secret_word_list[random.randint(0, len(secret_word_list)-1)]
secret_word_list = list(secret_word)
secret_word_set = set(secret_word_list)
guess_list = []
is_word_guessed = False

while is_word_guessed == False:
    guess_letter = input("Guess a letter: ")
    if guess_letter in secret_word:
        guess_list.append(guess_letter)
        print("Correct!", guess_letter,"is in the word")
    if guess_letter not in secret_word:
        print("X Try again X")
    if sorted(secret_word_set) == sorted(guess_list):
        is_word_guessed = True
    
print("You win ! The correct word is",secret_word)
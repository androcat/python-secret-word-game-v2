# Level Two
# Let's start using some of those cool data structures! For this level, create a data structure 
# that can hold a series of words, and let the game randomly select a word at the beginning of the game.
import random

words = ["kittens", "babies", "puppies", "happy", "nothing", "effervescent"]

secret_word = words[random.randint(0, len(words)-1)]
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
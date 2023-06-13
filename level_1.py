# Level One
# Your first attempt should be pretty straightforward. Choose a word you'd like to "guess", 
# and hardcode that word into your script. Create an input loop that asks for a letter and confirms 
# whether that letter exists in the chosen word or not on each round. Once the whole word has been 
# revealed, you win the game.

secret_word = "cohort"
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
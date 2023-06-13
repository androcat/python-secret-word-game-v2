# Secret Word Guesser

This challenge asks you to guess a word the computer has chosen. You'll work up to a limited number of tries before you lose the game!

## Objectives

### Learning Objectives

After completing this assignment, you should be able to...

* Write simple, well-organized CLI applications in Python
* Hand long-running user input loops
* Draw data from small collections

## Details

### Deliverables

* A repo containing at least one Python script (.py) per level (four total, minimum).

## I'm a Python Developer Mode

_Please fork this repo & complete each level in separate script file. Name each file in a way that makes the level clear (ex: `level_1.py`)._

### Level One
Your first attempt should be pretty straightforward. Choose a word you'd like to "guess", and hardcode that word into your script. Create an input loop that asks for a letter and confirms whether that letter exists in the chosen word or not on each round. Once the whole word has been revealed, you win the game.

### Level Two
Let's start using some of those cool data structures! For this level, create a data structure that can hold a series of words, and let the game randomly select a word at the beginning of the game. 

### Level Three
Let's make this more personal. In level three, separate your word choices into "easy", "medium", and "hard". Allow the player to select a difficulty level & select their word to guess from the corresponding data structure. _Hint: you might classify difficulty length of words, since there's more to guess.

### Level Four
Time for consequences! Add the "Hangman" feature to your game: after a certain number of tries, you lose the game and have to start over. 

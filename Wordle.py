#imports all the functions from wordle_functions.py to be used in this file with the prefix
#ws
import wordle_functions as wf

#list of five-letter words that the computer will choose from to be the secret word
word_list = [
    "crane", "train", "plant", "house", "mouse", "smile", "brush", "chair", "table", "board", 
    "shark", "whale", "pluck", "track", "black", "white", "brown", "blunt", "clout", "scout",
    "stare", "stone", "stand", "strap", "smart", "shirt", "short", "shout", "shone", "shove",
    "shake", "share", "sharp", "shear", "shelf", "shift", "shine", "shiny", "shoal", "shore",
    "shorn", "shrub", "shrug", "sight", "sigma", "silky", "siren", "skate", "skirt", "slate",
    "slice", "slide", "slime", "sling", "slope", "sloth", "smoke", "snake", "snare", "sneak",
    "snort", "snowy", "soapy", "sober", "solar", "solid", "solve", "sonic", "sound", "south",
    "space", "spade", "spark", "speak", "spend", "spice", "spike", "spine", "spite", "split",
    "spoil", "spoke", "sport", "spray", "squad", "squat", "stack", "stage", "stamp", "stark",
    "steam", "sting", "stink", "stole", "stove", "straw", "stray", "strip", "stuck", "study"
]

#Assigns the number of rounds to be played in the game and chooses a secret word from the list
rounds = 6
secret_word = wf.choose_word(word_list)

#Sets up the game and displayes the rules, and what the feedback letters mean.
print("Welcome to Mystery Wordle!")
print(f"\nGuess the five-letter word.")
print(f"\nG = correct letter and position.")
print(f"Y = correct letter, wrong position.")
print(f"- = letter is not in the word.\n")

#starts the good_guess variable at 1 and creates an empty list to store the guessed words
good_guess = 1
guessed_words = []

#Starts the game loop, which will run until the user has guessed the word or has used all
#the 6 rounds
while good_guess <= rounds:
    print(f"Attempt {good_guess} of {rounds}")
    #runs get_guess() function to get user input until it is a valid five-letter word
    guess = wf.get_guess()
    if guess is None:
        continue
    #append guess. If get_guess() == previous guess, then it will throw an error and ask for a new guess
    if guess in guessed_words:
        print("You've already guessed that word. Please try again.")
        continue
    #appends valid words that have already been guessed
    guessed_words.append(guess)
    feedback = wf.evaluate_guess(secret_word, guess)
    result = wf.has_won(secret_word, guess)
    #displays the guess and feedback for the guess
    wf.display_guess(guess, feedback)
    #checks to see if the guess matches the secret word or if the user has used all their
    #rounds, if so it will display the matching result and break the loop,
    #otherwise it will incrememt the good_guess variable by 1 and continue the loop
    if guess == secret_word or good_guess == (rounds):
        print(result)
        break
    else:
        good_guess += 1
    
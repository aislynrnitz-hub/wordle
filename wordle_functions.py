import random

#gets a random word from the list of words and returns it as the secret word
def choose_word(word_list):
    secret_word = random.choice(word_list)
    return secret_word

#Checks to make sure the user inputs a five-Letter word, if not it returns None, if it is
#valid it returns the word
def get_guess():
    user_guess = input("Enter a five-Letter word: ").lower()
    if len(user_guess) != 5:
        print("Please enter a five-Letter word.")
        return None
    else:
        return user_guess
    
#evaluates the guess against the secret word, determines the feedback for each letter,
#and returns that feedback as a string
def evaluate_guess(secret_word, guess):
    feedback = ""
    for i in range(0,5):
        if guess[i] == secret_word[i]:
            feedback += "G "
        elif guess[i] in secret_word:
            feedback += "Y "
        else:
            feedback += "- "
    return feedback

#Displays the guess in capital letters and the feedback for the guess
def display_guess(guess, feedback):
    print(f"Guess: {guess.upper()}")
    print(f"Feedback: {feedback}")

#If the guess is the secret word, returns a winning message, otherwise returns a 
#losing message revealing the secret word
def has_won(secret_word, guess):
    if guess == secret_word:
        return "You won!"
    else:
        return f"You Lost! The secret word was: {secret_word}"
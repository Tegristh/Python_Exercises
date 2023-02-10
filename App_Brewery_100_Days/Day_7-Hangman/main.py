# #Step 5
import random
import hangman_words
import hangman_art
from replit import clear


word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
message = ""
warning = ""
lives = 6
guessed = []
print(hangman_art.logo)
# #Testing code
#print(f'Pssst, the solution is {chosen_word}.')
#Create blanks
display = []
for _ in range(word_length):
    display += "_"
def ask_guess():
    return input("Guess a letter: ").lower()

def is_game_finished():
    if "_" not in display:
        return True, "You win"
    elif lives <= 0:
        return True, "You loose"
    else:
        return False, ""
    
def check_letters(char):
    if chosen_word.count(char) == 0:
        return 1, "the letter you guessed is not in the word, you lose a life"
    else:
        return 0, ""
    
#Check guessed letter
def replace_letters(char):
    position = 0
    for letter in chosen_word:
        if letter == char:
            display[position] = char
        position += 1

#run the game

while not end_of_game:
    guess = ask_guess()
    clear()
    if guess not in guessed:
        guessed += guess
        replace_letters(guess)
        life_modifier, warning = check_letters(guess)
        lives -= life_modifier
        end_of_game, message = is_game_finished()
    else:
        print(f"You already picked the letter {guess}")
        print(warning)
    warning = ""
    print(f"{' '.join(display)}")
    print(hangman_art.stages[lives])
    print(message)
print(f"The Word was {chosen_word}")

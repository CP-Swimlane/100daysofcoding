import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear
from termcolor import colored, cprint
from play_sounds import bell, bell_after

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)
guessed = []
display = []
for _ in range(word_length):
    display += "_"
    

while not game_is_finished:
    guess = input("Guess a letter: ").lower()
    print("\n")
    print(f"\nYour past guesses - {guessed}\n")
    print("\n")
    #Use the clear() function imported from replit to clear the output between guesses.
    clear()
    print(logo)
    guessed.append(guess)
    print(f"Your past guesses - {guessed}")
    if guess in display:
        print(f"You've already guessed '{guess}'.")
               

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print(f"You lose. Word was {chosen_word}")
    
    if not "_" in display:
        game_is_finished = True
        
        print(f'''Word was {chosen_word} \n''')      

        # play bell
        bell()

        cprint('\n  Brilliant!! YOU WIN!! ', 'red', attrs=['bold','blink'])
        

    print(stages[lives])
    if game_is_finished:
        again = input("Would you like to play again? (yes or no): ")
        if again == "yes":
            print(logo)
            game_is_finished = False
            lives = len(stages) - 1
            
            chosen_word = random.choice(word_list)
            print(chosen_word)
            word_length = len(chosen_word)
            guesses = 0
            guessed = []
            display = []
            for _ in range(word_length):
                display += "_"
            clear()
            print(logo)
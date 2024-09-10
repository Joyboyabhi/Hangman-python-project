import random #import "random" module so that we can generate a random word
import hangman_stages
import word_file

lives = 6 #limit for guessing the word.

chosen_word = random.choice(word_file.word) #choose a random word from the list and store it in the "chossen_word"

print(chosen_word)

display=[]
for letter in chosen_word: #or use "for i in range(len(chosen_word))"
    display +='_'#take a empty  list "display" and create a for loop so that the '_' are displayed for each letter insted of the letter itself.

print(display)
game_over=False #create a variable "game_over" so that we can limit the ammount of guesses. and add function in a while loop
while not game_over:
    guessed_letter=input("guess a letter: ").lower() #ask for user i/p and convert to lower case
    for position in range(len(chosen_word)):#crete ranges 0 1 2 3 4 5 6.......
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -= 1 #cut one life if chossen wrong word.
        if lives ==0:
            game_over = True
            print("you loose!!!") #if all lives are used then game over
    if '_'not in display:
        game_over = True
        print("YOU WIN!!!") #if guessed correctly within give lives you win
    print(hangman_stages.stages[lives])
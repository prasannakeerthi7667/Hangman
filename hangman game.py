import random#for random
import hangman_stages
word_list=["apple","banana","carrot"]#taken list
chosen_word=random.choice(word_list)#choosing random value
lives=6
print(chosen_word)#printing it
display=[]#taking empty list
for i in range(len(chosen_word)):
    display += '_'
print(display)#printing the number of blanks in place of chose_word letters
game_over=False
while not game_over:
    guessed_letter=input("guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -=1
        if lives==0:
            game_over=True
            print("you lose!!")
    if '_' not in display:
        game_over=True
        print("you win!!")
    print(hangman_stages.stages[lives])

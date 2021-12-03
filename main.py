import random
from words import words
from visual import lives_visual_dict
import string

def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word= random.choice(words)
    
    return word.upper()

def hangman():
    word =get_valid_word(words)
    word_letters =set(word)
    alphabet =set(string.ascii_uppercase)
    used_letters =set()

    lives=7 

    #getting user input
    while len(word_letters)>0 and lives>0:
        #letters used
        print('You have', lives, 'lives left and you have used these letters:', ' '.join(used_letters))

        #what the current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word:', ' '.join(word_list))

        user_letter =input('Guess a letter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives=lives-1
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that character. Guess abother letter.')

        else:
            print('\nInvalid Character. Pleave try again')

    #get here when len(word_letter)==0 or when lives==0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')

if __name__=='__main__':
    hangman()

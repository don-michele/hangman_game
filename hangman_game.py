### Hangman game!

import random

# Part 1 - Pick Word

def createWordList():  # Create the list of words to pick from

    word_list = []
    word_file = open('sowpods.txt', 'r')

    for word in word_file:
        word_list.append(word)

    word_file.close()

    return word_list

def pickRandomWord(word_list):  # Select a random word from the list

    selected_word = word_list[random.randint(0, len(word_list) - 1)].strip()

    return selected_word

# Part 2 - Guess Letters

def showHeader():

    print("""
  _   _                                         
 | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 |  _  | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    |___/                       
          """)



def showMaskedWord(selected_word):

    mask = '_'
    word_length = len(selected_word)

    # Print the masked word
    showHeader()
    print(50 * '-')
    print()
    print('The below word has been chosen!')
    # print('Selected word: ', selected_word) ### Uncomment to see the chosen word!
    masked_word = mask * word_length

    return masked_word

def showCurrentStateOfWord(masked_word_letter_list):
    current_checked_word = " ".join(masked_word_letter_list)
    print()
    print(current_checked_word)
    print()

def showMessageAlert(message, selected_word):
    if (message == 'Win'):
        print('Congratulations!\nYou won!')
    elif (message == 'Go on'):
        print('\nGood! Keep going!')
    elif (message == 'Lose'):
        print('\nIncorrect choice!\nNo more guesses left! You lost!' \
              '\nThe word was', selected_word)
    elif (message == 'Wrong'):
        print('\nIncorrect choice!')
    elif (message == 'Invalid'):
        print('This is not a letter! Try again!')
    else:
        print('No available message!')

def showGraphicHangman(guesses_left):
    if (guesses_left == 6):
        print("""
     _________
     |/      |
     |      
     |       
     |        
     |       
     |
  ___|____

              """)

    elif (guesses_left == 5):
        print("""
     _________
     |/      |
     |      (_)
     |       
     |        
     |       
     |
  ___|____
              """)

    elif (guesses_left == 4):
        print("""
     _________
     |/      |
     |      (_)
     |       |
     |       |
     |       |
     |       
  ___|____
              """)

    elif (guesses_left == 3):
        print("""
     _________
     |/      |
     |      (_)
     |       |
     |      /|
     |       |
     |       
  ___|____
              """)

    elif (guesses_left == 2):
        print("""
     _________
     |/      |
     |      (_)
     |       |
     |      /|\ 
     |       |
     |       
  ___|____
              """)

    elif (guesses_left == 1):
        print("""
     _________
     |/      |
     |      (_)
     |       |
     |      /|\ 
     |       |
     |      /
  ___|____

              """)
    elif (guesses_left == 0):
        print("""
     _________
     |/      |
     |      (_)
     |       |
     |      /|\ 
     |       |
     |      / \ 
  ___|____

              """)
    else:
        print()

def showLetterReport(already_correct, already_incorrect, guesses_left):
    correct_string = 'Correct guesses: ' + already_correct
    incorrect_string = 'Wrong guesses: ' + already_incorrect
    guesses_left_string = 'Misses left: ' + str(guesses_left)
    print()
    print('+', 38 * '-', '+')
    print('|', 38 * ' ', '|')
    print('|', correct_string.center(38), '|')
    print('|', incorrect_string.center(38), '|')
    print('|', guesses_left_string.center(38), '|')
    print('|', 38 * ' ', '|')
    print('+', 38 * '-', '+')
    print()

def guessLetters(selected_word, masked_word):
    selected_word_letter_list = list(selected_word)
    masked_word_letter_list = list(masked_word)
    showCurrentStateOfWord(masked_word_letter_list)
    guesses_left = 6
    already_correct = ''
    already_incorrect = ''
    user_guess = input('Guess the letter: ')

    while ((masked_word_letter_list.count('_') != 0) and (guesses_left > 0)):

        letter_index_list = []

        if (user_guess.isalpha() == True):
            if (user_guess.upper() in selected_word):
                already_correct += user_guess.upper()
                for index in range(0, len(selected_word_letter_list)):
                    if (user_guess.upper() == selected_word_letter_list[index]):
                        letter_index_list.append(index)

                for element in letter_index_list:
                    masked_word_letter_list[element] = user_guess.upper()
                showCurrentStateOfWord(masked_word_letter_list)

                showGraphicHangman(guesses_left)

                if (masked_word_letter_list.count('_') == 0):
                    showMessageAlert('Win', selected_word)
                    showLetterReport(already_correct, already_incorrect, guesses_left)
                else:
                    showMessageAlert('Go on', selected_word)
                    showLetterReport(already_correct, already_incorrect, guesses_left)
                    user_guess = input('Guess the letter: ')
            else:
                if (user_guess.upper() not in already_incorrect):
                    already_incorrect += user_guess.upper()
                    guesses_left -= 1

                if (guesses_left == 0):
                    showGraphicHangman(guesses_left)
                    showMessageAlert('Lose', selected_word)
                    showLetterReport(already_correct, already_incorrect, guesses_left)
                else:
                    showCurrentStateOfWord(masked_word_letter_list)
                    showGraphicHangman(guesses_left)
                    showMessageAlert('Wrong', selected_word)
                    showLetterReport(already_correct, already_incorrect, guesses_left)
                    user_guess = input('Guess the letter: ')
        else:
            showCurrentStateOfWord(masked_word_letter_list)
            showMessageAlert('Invalid', selected_word)
            user_guess = input('Guess the letter: ')

def playGame():
    word_list = createWordList()
    selected_word = pickRandomWord(word_list)
    masked_word = showMaskedWord(selected_word)
    guessLetters(selected_word, masked_word)



def main():

    playGame()

main()
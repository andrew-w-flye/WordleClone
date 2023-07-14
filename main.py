import random

tries = 0
game_on = True
PURPLE = '\033[95m'
END = '\033[0m'
GREEN = '\033[92m'
RED = '\033[0;31m'
YELLOW = '\033[0;93m'

correctPosition = []
wrongPosition = []
notInWord = []
letters = 'abcdefghijklmnopqrstuvwxyz'

print('Welcome to Wordle Clone! If the letter is green, it is the correct letter in the correct spot. If the letter is yellow, it is the correct letter in the wrong spot. If the letter is white, that letter is NOT in the word.\n\n')

def generate_word():
  wordList = open("word_list.txt").read().split()
  word = random.choice(wordList)
  return word

def get_guess():
  guess = input('What is your guess? ')
  if len(guess) != 5:
    print('Please enter a 5 letter word')
    get_guess()
  else:
    return guess

def compare_words(guess, word):
  correctLetters = 0
  coloredGuess = ''
  for i,letter in enumerate(guess):
    if letter in word:
      if guess[i] == word[i]:
        coloredGuess += (GREEN + letter + END)
        correctLetters += 1
        if letter not in correctPosition:
          correctPosition.append(letter)
      else:
        coloredGuess += (YELLOW + letter + END)
        if letter not in wrongPosition and letter not in correctPosition:
          wrongPosition.append(letter)
    else:
      coloredGuess += (letter)
      if letter not in notInWord:
        notInWord.append(letter)
  print (coloredGuess + '\n')
  return correctLetters

def print_letters():
  printLetters = ''
  for letter in letters:
    if letter in correctPosition:
      printLetters += (GREEN + letter + END + ' ')
    elif letter in wrongPosition:
      printLetters += (YELLOW + letter + END + ' ')
    elif letter in notInWord:
      printLetters += (RED + letter + END + ' ')
    else:
      printLetters += (letter + ' ')
  print('Available Letters: \n' + printLetters + '\n')
word = generate_word()

while game_on:
  print_letters()
  print('You have ' + str(5 - tries) + ' tries left')
  guess = get_guess()
  correctLetters = compare_words(guess,word)
  if correctLetters == 5:
    print('You win!')
    game_on = False
  else:
    tries += 1
  if tries > 4:
    print('You lose')
    print('The word was ' + GREEN + word + END)
    game_on = False
  
import random

def GameStart(start):
    start = 'end'
    answer = wordBank[random.randint(0, len(wordBank) - 1)]
    print('Let\'s get started! \nTry to get all the letters or guess the word! \n*HINT* There are NOT any CAPITAL letters \nIf you get seven wrong, it\'s Game Over! \n\t\tGood Luck!')
    GamePlay(answer, start)
    return(start)


def GamePlay(answer, start):
    wrongCount = 0
    uGuess = ''
    progress = ['_'] * len(answer)
    built = ''
    # print(answer)
    while wrongCount < len(gallows):
        print(gallows[wrongCount])
        for i in progress:
            print(i, end=' ')
        print()
        uGuess = input('Guess a letter, or type \"Guess\" to solve the word:  ')
        if len(uGuess) > 1:
            if uGuess == 'Guess' or uGuess == 'guess':
                uGuess = input('Type in your word:   ')
                if uGuess == answer:
                    if wrongCount < 1:
                        print('Did you CHEAT?!')
                        print('Good Job I guess.')
                        break
                    else:
                        print('Thats it!!! You win! Good Job!')
                        break
                else:
                    wrongCount += 1
                    print('That\'s not it!')
            else:
                print('One letter at a time, please')
                uGuess = ''
        elif uGuess in answer:
            for i in range(len(answer)):
                if uGuess == answer[i]:
                    progress[i] = uGuess
            print('Thats good, you got one!')
            uGuess = ''
            built = ''.join(progress)
            if built == answer:
                print(built)
                print('Thats it!!! You win! Good Job!')
                break    
        elif uGuess not in answer:
            print('Bad luck, kid. Try again')
            wrongCount += 1
            uGuess = ''
        


    



wordBank = ['sword', 'dungeons', 'dragons', 'dungeon', 'dragon', 'critical', 'dodecahedron', 'dice', 
'cleric', 'rogue', 'paladin', 'candle', 'spell', 'wizard']

gallows = ['''

  +---+
      |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


print('Welcome to hangman!')
start = input('Would you like to play a game? [Y/N]')
while True:
    if start.lower() == 'y':
        start = GameStart(start)
    elif start.lower() == 'n':
        print('Bye!')
        break
    elif start == 'end':
        start = input('Play again? [Y/N]')
    else:
        print('Try again!')
        start = input('Would you like to play a game? [Y/N]')
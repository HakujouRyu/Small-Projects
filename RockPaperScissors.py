import random


def com():
    comthrow = ['r', 'p', 's']
    return (random.choice(comthrow))


def score(x):
    comScore = 0 
    playerScore = 0
    playCount = 0
    if x == 'c':
        comScore += 1
    elif x == 'p':
        playerScore += 1
    else:
        pass
    playCount += 1
    print('Player Score:', playerScore, 'Computer Score:', comScore)


def compare(p1, c):
    if p1 == 'r':
        if c == 'r':
            print('Draw!')
            score('d')
        elif c == 'p':
            print('Computer wins!')
            score('c')
        elif c == 's':
            print('Player One wins!')
            score('p')
    elif p1 == 'p':
        if c == 'r':
            print('Player One Wins!')
            score('p')
        elif c == 'p':
            print('Draw!')
            score('d')
        elif c == 's':
            print('Computer wins')
            score('c')
    elif p1 == 's':
        if c == 'r':
            print('Computer wins!')
            score('c')
        elif c == 'p':
            print('Player One wins!')
            score('p')
        elif c == 's':
            print('Draw!')
            score('d')


def player_choice():
    comChoice = com()
    # print(comChoice)
    options = ['r', 'p', 's']
    while True:
        choice = input('Enter choice: ')
        if choice.lower() not in options:
            print('try again')
            continue
        else:
            break
    compare(choice, comChoice)


print('Welcome to Rock Paper Scissors!')
print('Enter "r" for Rock, "p" for Paper, and "s" for Scissors!')
player_choice()
while True:
    rerun = input('Play again? [Y/N]: ')
    if rerun.lower() != 'y' and rerun.lower() != 'n':
        print('"Y" or "N"')
        continue
    elif rerun.lower() == 'y':
        player_choice()
    elif rerun.lower() == 'n':
        break

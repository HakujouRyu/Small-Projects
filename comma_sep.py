def list_string(ls):
    for item in ls: 
        print(item, sep='')


def printcol(ar):
    for y in range(len(ar[0])):
        for x in range(len(ar)):
            print(ar[x][y],sep='')
        print()




spam = ['apples', 'bananas', 'tofu', 'cats']


grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
    ]


#TIC-TAC-TOE

board = [' ' for x in range(10)]
def insertletter(letter, pos):
    board[pos]=letter
    
def spaceisfree(pos):
    return board[pos]==' '

def printboard(board):
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |   ')
    print('----------')
    print('   |   |   ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |   ')
    print('----------')
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |   ')
    
def iswinner(bo, le):
    return (bo[7]==le and bo[8]==le and bo[9] == le) or (bo[4]==le and bo[5]==le and bo[6] == le) or (bo[1]==le and bo[2]==le and bo[3] == le) or (bo[1]==le and bo[4]==le and bo[7] == le) or (bo[2]==le and bo[5]==le and bo[8] == le) or(bo[3]==le and bo[6]==le and bo[9] == le) or (bo[1]==le and bo[5]==le and bo[9] == le) or (bo[3]==le and bo[5]==le and bo[7] == le)

def playermove():
    run = True
    while run:
        move = input('Please, Select a position to place an\'x\'(1-9):')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceisfree(move):
                    run = False
                    insertletter('X', move)
                else:
                    print('Sorry this space is occupied!')
            else:
                print('Please, type a number within the range of 10')
                
        except:
            print('Please type a number')
            
def compmove():
    possiblemoves = [x for x, letter in enumerate(board) if letter==' ' and x!=0]
    move = 0

    for let in ['O', 'X']:
        for i in possiblemoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if iswinner(boardcopy, let):
                move = i
                return move
    corner = []
    for i in possiblemoves:
        if i in [1,3,7,9]:
            corner.append(i)
    if len(corner) >0:
        move = selectrandom(corner)
        return move

    if 5 in possiblemoves:
        move = 5
        return move

    edge = []
    for i in possiblemoves:
        if i in [2,4,6,8]:
            edge.append(i)
    if len(edge) >0:
        move = selectrandom(edge)

def selectrandom(li):
    import random

    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def isfull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
    
def main():
    print("Welcome To Tic Tac Toe!")
    printboard(board)
    while not(isfull(board)):
        if not(iswinner(board, 'O')):
            playermove()
            printboard(board)
        else:
            print("Sorry, 0\'s won this Time")
            break
        if not(iswinner(board, 'X')):
            move = compmove()
            if move == 0:
                print('Tie Game!')
            else:
                insertletter('O', move)
                print('Computer places an \'O\' in position', move, ':')
                printboard(board)
        else:
            print("X\'s won this Time")
            break

    if isfull(board):
        print('Tie Game!')


main()

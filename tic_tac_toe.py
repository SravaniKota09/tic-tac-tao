import sys
board=[' ',' ',' ',
       ' ',' ',' ',
       ' ',' ',' ']

player1='X'
player2='O'

print('Player1 is X')
print('Player2 is O')
def displayBoard(board):
    print(board[0],'|',board[1],'|',board[2])
    print('---------')
    print(board[3],'|',board[4],'|',board[5])
    print('---------')
    print(board[6],'|',board[7],'|',board[8])
    
def checkRow(board):
    if board[0]==board[1]==board[2] and board[0]!=' ':
        if board[0]=='X':
            print('Player1 is winner')
        else:
            print('Player2 is winner')
        return True
    if board[3]==board[4]==board[5] and board[3]!=' ':
        if board[3]=='X':
            print('Player1 is winner')
        else:
            print('Player2 is winner')
        return True
    if board[6]==board[7]==board[8] and board[6]!=' ':
        if board[6]=='X':
            print('Player1 is winner')
        else:
            print('Player2 is winner')
        return True
    return False

def checkCol(board):
    if board[0]==board[3]==board[6] and board[0]!=' ':
        if board[0]=='X':
            print('Player1 is winner')
        else:
            print('Player2 is winner')
        return True
    if board[1]==board[4]==board[7] and board[1]!=' ':
        if board[1]=='X':
            print('Player1 is winner')
        else:
            print('Player2 is winner')
        return True
    if board[2]==board[5]==board[8] and board[2]!=' ':
        if board[2]=='X':
            print('Player1 is winner')
        else:
            print('Player2 is winner')
        return True
    return False

def checkDiag(board):
    if board[0]==board[4]==board[8] and board[0]!=' ':
        if board[0]=='X':
            print('Player1 is winner')
        else:
            print('Player2 is winner')
        return True
    if board[2]==board[4]==board[6] and board[2]!=' ':
        if board[2]=='X':
            print('Player1 is winner')
        else:
            print('Player2 is winner')
        return True
    return False
for i in range(1,10):
    while(True):
        val=int(input('Enter a number between 1 to 9:'))
        if board[val-1]==' ' and val>=1 and val<=9:
            break
        else:
            print("Enter a valid number!!!!!")
    if i%2==1:
        board[val-1]=player1
    else:
        board[val-1]=player2
    displayBoard(board)
    if checkRow(board) or checkCol(board) or checkDiag(board):
        print("Game ended")
        sys.exit()

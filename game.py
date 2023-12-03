import random
board = [[' ',' ',' '] for i in range(3)]
player1Turn = True
moves = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

def displayBoard(board):
    for i in range(0,3):
        for j in range(0,3):
            if(j != 2) :
                print(board[i][j] ,end=" | ")
            else:
                print(board[i][j])
        if(i!=2):
            print("---"*3)

def checkWin(board):
    # horizontal
    for i in board:
        if ((['O','O','O'] == i) or (['X','X','X'] == i)):
            return True
    # vertical
    for i in range(3):
        ver = [board[0][i],board[1][i],board[2][i]]
        if ((['O','O','O'] == ver) or (['X','X','X'] == ver)):
            return True
    # diagonally
    diagonal1 = [board[0][0],board[1][1],board[2][2]]
    if ((['O','O','O'] == diagonal1) or (['X','X','X'] == diagonal1)):
        return True
    
    diagonal2=[board[0][2],board[1][1],board[2][0]]
    if ((['O','O','O'] == diagonal2) or (['X','X','X'] == diagonal2)):
        return True
    return False
    
def boardFull(board):
    for i in board:
        if(' ' in i):
            return False
    return True


while not boardFull(board):
    if(player1Turn):
        player1Turn = not player1Turn  
        (comp1x,comp1y) = random.choice(moves)
        board[comp1x][comp1y] = 'O'
        moves.remove((comp1x,comp1y))
        displayBoard(board)
        print()
        if checkWin(board):
            print("Computer 1 wins")
            exit()
    else :
        player1Turn = not player1Turn
        (comp2x,comp2y) = random.choice(moves)
        board[comp2x][comp2y] = 'X'
        moves.remove((comp2x,comp2y))
        displayBoard(board)
        print()
        if checkWin(board):
            print("Computer 2 wins")
            exit()

print("Its a Tie")
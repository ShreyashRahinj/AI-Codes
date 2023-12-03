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
        compChoice = random.randint(0,8)
        if(moves[compChoice] != (-1,-1)):
            player1Turn = not player1Turn  
            board[moves[compChoice][0]][moves[compChoice][1]] = 'O'
            moves[compChoice] = (-1,-1)
            displayBoard(board)
            print()
            if checkWin(board):
                print("Computer wins")
                exit()
    else :
        playerChoice = int(input())
        x,y = moves[playerChoice-1]
        if((x,y) != (-1,-1)):
            board[x][y] = 'X'
            moves[playerChoice-1] = (-1,-1)
            displayBoard(board)
            print()
            if checkWin(board):
                print("Player wins")
                exit()
            player1Turn = not player1Turn
        else:
            print("Position already in use")

print("Its a Tie")
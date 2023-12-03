def solve(board):
    n = len(board)
    row = -1
    col = -1

    emptyleft = True

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                row = i
                col = j
                emptyleft = False
                break
    
        if emptyleft == False:
            break
    
    if emptyleft == True:
        return True
    
    for number in range(1,10):
        if(isSafe(board,row,col,number)):
            board[row][col] = number
            if(solve(board)):
                return True
            else:
                board[row][col] = 0

    return False

def isSafe(board,row,col,num):
    for i in range(len(board[row])):
        if board[row][i] == num:
            return False
    for i in range(len(board)):
        if(board[i][col] == num):
            return False
    return True

def displayBoard(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=" ")
        print()

n = 3
board = [[0 for i in range(n)] for i in range (n)]

if solve(board):
    displayBoard(board,n)
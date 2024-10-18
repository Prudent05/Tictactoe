# A Program To Create The Tic-Tac-Toe Game
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# take player input
def playerInput(board):
    inp = int(input("Enter a number 0-8: "))
    if inp >= 0 and inp <= 8 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("UHoh player is already in that spot")
# check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[2]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winner = board[7]
        return True
    
def checkColumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[7] != "-":
        winner = board[7]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[5]
        return True
    
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

def checkWin():
    if checkDiagonal(board) or checkColumn(board) or checkHorizontal(board):
        print(f"The winner is {winner}")

#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "0"
    else:
        currentPlayer = "X"
# check for win or tie again

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
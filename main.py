gameRun = True
currentPlayer = "X"
winner = None

# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]


def displayBoard():		# Display the game board to the screen
    print(' ' + board[0] + " | " + board[1] + " | " + board[2])
    print(' ' + board[3] + " | " + board[4] + " | " + board[5])
    print(' ' + board[6] + " | " + board[7] + " | " + board[8])


def handleTurn(currentPlayer):  # Handle a turn for an player

    # Get position from player
    print(" " + currentPlayer + "'s turn.")
    position = input(" Choose a Position from 1-9: ")

    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input(" Choose a Position from 1-9: ")

        # Get correct index in our board list
        position = int(position) - 1

        # make sure the spot is available on the board
        if board[position] == "-":
            valid = True
        else:
            print(" Place Already Filled. Choose Again")

    board[position] = currentPlayer
    displayBoard()


def gameOver():
    win()
    isTie()


def win():
    # Global variables
    global winner

    # if there was a winner anywhere
    rowWinner = rows()
    colWinner = columns()
    diagWinner = diagonals()

    # Get the winner
    if rowWinner:
        winner = rowWinner
    elif colWinner:
        winner = colWinner
    elif diagWinner:
        winner = diagWinner
    else:
        winner = None


def isTie():
    global gameRun

    if "-" not in board:
        gameRun = False
        return True
    # Else there is no tie
    else:
        return False


def rows():
    global gameRun

# if any of the rows have all the same value
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

# If any row does have a match
    if row1 or row2 or row3:
        gameRun = False

        # Return the winner
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None


def columns():
    global gameRun

    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3:
        gameRun = False

    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return


def diagonals():
    global gameRun

    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"

    if diag1 or diag2:
        gameRun = False

    if diag1:
        return board[0]
    elif diag2:
        return board[6]
    return


def flipPlayer():
    global currentPlayer

# If the current player was X, make it O
    if currentPlayer == "X":
        currentPlayer = "O"

        # Or if the current player was O, make it X
    elif currentPlayer == "O":
        currentPlayer = "X"


def playGame():
    # Display Initial Board
    displayBoard()

# Loop until the game stops
    while gameRun:

        # Handle a turn
        handleTurn(currentPlayer)

        # Check if the game is over
        gameOver()

        # Flip to the other player
        flipPlayer()

    if winner == "X" or winner == "O":
        print("\n " + winner + " Wins...!!")
    elif winner == None:
        print("\n Game Tie")


print('\n Welcome To Tic Tac Toe..!! \n')
playGame()

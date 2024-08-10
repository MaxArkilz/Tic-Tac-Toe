import sys
import os


def playBall():
    # main game engine
    # reset game board, start game loop
    print('Do you want to go first?')
    print('a) Yes, I\'ll go first.')
    print('b) No, you go ahead.')
    whosOnFirst = input('Type \'a\' or \'b\' ')
    gameBoard = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    isGameRunning = True
    
    while isGameRunning:

        # game turn tracker, depending on who goes first
        if whosOnFirst == 'a':
            playerSpot = playerTurn(gameBoard)
            gameBoard[playerSpot] = 'X'
            aiSpot = aiTurn(gameBoard)
            gameBoard[aiSpot] = 'O'

            # current game board, updated each loop
            print(f'         {gameBoard[1]}| {gameBoard[2]} | {gameBoard[3]}')
            print('         _  _  _')
            print(f'         {gameBoard[4]}| {gameBoard[5]} | {gameBoard[6]}')
            print('         _  _  _')
            print(f'         {gameBoard[7]}| {gameBoard[8]} | {gameBoard[9]}')

            # check game status
            if threeInRow(gameBoard) == 'xwin':
                theEnd('xwin')
                break

            elif threeInRow(gameBoard) == 'owin':
                theEnd('owin')
                break

            elif ' ' not in gameBoard.values():
                theEnd('tie')
                break

        elif whosOnFirst == 'b':
            aiSpot = aiTurn(gameBoard)
            gameBoard[aiSpot] = 'O'

            # current game board, updated each loop
            print(f'         {gameBoard[1]}| {gameBoard[2]} | {gameBoard[3]}')
            print('         _  _  _')
            print(f'         {gameBoard[4]}| {gameBoard[5]} | {gameBoard[6]}')
            print('         _  _  _')
            print(f'         {gameBoard[7]}| {gameBoard[8]} | {gameBoard[9]}')

            # check game status
            if threeInRow(gameBoard) == 'xwin':
                theEnd('xwin')
                break

            elif threeInRow(gameBoard) == 'owin':
                theEnd('owin')
                break

            elif ' ' not in gameBoard.values():
                theEnd('tie')
                break

            playerSpot = playerTurn(gameBoard)
            gameBoard[playerSpot] = 'X'


def threeInRow(board):
    # check if either side has won
    possibleWins = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7)
    ]

    for (a, b, c) in possibleWins:
        if board[a] == 'X' and board[b] == 'X' and board[c] == 'X':
            return 'xwin'

        if board[a] == 'O' and board[b] == 'O' and board[c] == 'O':
            return 'owin'

        else:
            return None



def playerTurn(board):
    # print guide for choosing move
    print()
    print('1 | 2 | 3')
    print('_  _  _')
    print('4 | 5 | 6')
    print('_  _  _')
    print('7 | 8 | 9')
    
    # provide user input
    print('Where would you like to go?')
    move = input('Type a number 1 - 9: ')
    
    # make sure input is valid
    if int(move) not in board:
        print('Invalid input, try again.')
        playerTurn(board)
        
    # make sure space is empty
    if board[int(move)] != ' ':
        print('That space is occupied, please choose a different spot.')
        playerTurn(board)
        
    # change board to player move
    return int(move)



def aiTurn(board):
    possibleWins = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7)
    ]

    # prioritize center play
    if board[5] == ' ':
        return 5


    for (a, b, c) in possibleWins:
        # check for wins
        if (board[a] == 'O' and board[b] == 'O') and board[c] == ' ':
            return c
        elif (board[a] == 'O' and board[c] == 'O') and board[b] == ' ':
            return b
        elif (board[b] == 'O' and board[c] == 'O') and board[a] == ' ':
            return a

        # check for blocks
        if (board[a] == 'X' and board[b] == 'X') and board[c] == ' ':
            return c
        elif (board[a] == 'X' and board[c] == 'X') and board[b] == ' ':
            return b
        elif (board[b] == 'X' and board[c] == 'X') and board[a] == ' ':
            return a

    else:
        # otherwise choose first avalible shop
        for space in board:
            if board[space] == ' ':
                return space


def theEnd(winner):
    # end game text and pause
    if winner == 'xwin':
        print('Congradulations! You won!')

    elif winner == 'owin':
        print('Hooray, I won!')

    elif winner == 'tie':
        print('Look\'s like a cat\'s game')

    input('Press enter to continue')
    mainMenu()


def mainMenu():
    # Provide main menu to play a game or exit the program
    print('Hello! Welcome to the Tic Tac Toe Machine.')
    print('Do you want to play a game?')
    
    while True:
        playerChoice = input('Type \'yes\' or \'no\' ')
        if playerChoice.lower() == 'yes':
            playBall()
            break
        elif playerChoice.lower() == 'no':
            print('Okay, goodbye!')
            input('Press enter to exit ')
            break
        else:
            print('That is not a valid option. Please type \'yes\' or \'no\'')
            print()


if __name__ == '__main__':
    mainMenu()

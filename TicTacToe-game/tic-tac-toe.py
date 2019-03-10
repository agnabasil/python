import random

def display_board(board):

    #the board which is passed is a list 
    print('\n'*100) #clear the board history
    avail = [str(num) for num in range(0,10)]

    for i,val in enumerate(board):
        if val != ' ':
            avail[i] = ' '
    print('Game board' + '\t' + 'Available Moves')    
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + '\t' + ' ' + avail[7] + ' | ' + avail[8] + ' | ' + avail[9])
    print('-----------' + '\t' + '-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + '\t' + ' ' + avail[4] + ' | ' + avail[5] + ' | ' + avail[6])
    print('-----------'+ '\t' +'-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + '\t' + ' ' + avail[1] + ' | ' + avail[2] + ' | ' + avail[3])

# test_board = ['#','X','X','X','O','X','X','X','O','O']
# display_board(test_board)

def player_input():
    marker = ''
    player1_name = input('player 1 , What should i call you?')
    player2_name = input('And player 2 , What should i call you?')
    while not (marker == 'X' or marker == 'O'):
        marker = input('{}, please select your side X or O:-\t~'.format(player1_name)).upper()

    if marker == 'X':
        print('So, {} has choosen {} and {} will be {} side\'s for this game!'.format(player1_name,'X',player2_name,'O'))
        return ('X','O',player1_name,player2_name) #player 1 = 'X' and player 2 = 'O'
    else:
        print('So, {} has choosen {} and {} will be {} side\'s for this game!'.format(player1_name,'O',player2_name,'X'))
        return ('O','X',player1_name,player2_name) #player 1 = 'O' and player 2 = 'X'

# player_input()
# player1,player2 = player_input()
# print(player1,player2)

def place_marker(board, marker, position):
    board[position] = marker

# place_marker(test_board,'$',5)
# display_board(test_board)

def win_check(board,mark):
    return((board[1] == mark and board[2] == mark and board[3] == mark) or #first row
    (board[4] == mark and board[5] == mark and board[6] == mark) or #second row
    (board[7] == mark and board[8] == mark and board[9] == mark) or #third row
    (board[1] == mark and board[4] == mark and board[7] == mark) or #first column
    (board[2] == mark and board[5] == mark and board[8] == mark) or #second column
    (board[3] == mark and board[6] == mark and board[9] == mark) or #third column
    (board[1] == mark and board[5] == mark and board[9] == mark) or #diagonal 1
    (board[3] == mark and board[5] == mark and board[7] == mark)) #diagonal 1


# check = win_check(test_board,'X')
# print(check)
# display_board(test_board)

def choose_first():
    if random.randint(0, 1) == 0:
        return p2_name
    else:
        return p1_name

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose your next position: (1-9) '))
    
    return position

def replay():
    return input('Do you want to play again: Enter Yes or No:\t~').lower().startswith('y')


print('Welcome to Tic Tak Toe')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker,p1_name,p2_name = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == p1_name:
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! {} has won!'.format(p1_name))
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = p2_name
        
        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! {} has won!'.format(p2_name))
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = p1_name
        
    if not replay():
        break    
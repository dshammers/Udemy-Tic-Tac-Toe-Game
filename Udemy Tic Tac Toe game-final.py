from IPython.display import clear_output
def display_board():
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
def player_input():
    while True:
        marker=input('Player 1, choose X or O: ').upper()
        if marker=='X':
            return ('X','O')
        if marker=='O':
            return('O','X')
def place_marker(board, marker, position):
    board[position]=marker
def win_check(board,mark):
    if board[7]==board[8]==board[9]==mark:
        return True
    if board[4]==board[5]==board[6]==mark:
        return True
    if board[1]==board[2]==board[3]==mark:
        return True
    if board[7]==board[5]==board[3]==mark:
        return True
    if board[9]==board[5]==board[1]==mark:
        return True
    if board[7]==board[4]==board[1]==mark:
        return True
    if board[8]==board[5]==board[2]==mark:
        return True
    if board[9]==board[6]==board[3]==mark:
        return True
    return False
import random
def choose_first():
    if random.randint(1,2)==1:
        return 'Player 1'
    return 'Player 2'
def space_check(board,position):
    if board[position]==' ':
        return True
    return False
def full_board_check(board):
    if ' ' not in board:
        return True
    return False
def player_choice(board):
    position=0
    while position not in range(1,10) or not space_check(board,position):
        position=int(input("What space would you like to play? Pick from 1-9:   "))
    return position
def replay():
    response=''
    while True:
        response=input('Do you want to play again? y/n')
        if response=='y':
            return True
        elif response == 'n':
            return False
            print('game over!')
#while loop to keep running the game
print('Welcome to Tic Tac Toe!')

while True:
    # play game here
    
    ##set up the game (who's first, pick markers, etc)
    board=[' ']*10
    board[0]='#'
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    game_on=True
    print(turn+' will go first')
    play_game=input('Want to play? y/n')
    if play_game=='y':
        game_on=True
    else:
        game_on=False
    #play game
    while game_on:
        if turn=='Player 1':
        #player one turn
        #show board
            display_board()
            #choose position
            position=player_choice(board)
            #place marker on position
            place_marker(board,player1_marker,position)
            #win check
            if win_check(board,player1_marker):
                    display_board()
                    print('player 1 has won!')
                    game_on=False
            else:
                if full_board_check(board):
                    display_board()
                    print('Tie game!')
                    game_on=False
                else:
                    turn='Player 2'
        #player two turn
        else:
        #player one turn
        #show board
            display_board()
        #choose position
            position=player_choice(board)
        #place marker on position
            place_marker(board,player2_marker,position)
        #win check
            if win_check(board,player2_marker):
                display_board()
                print('player 2 has won!')
                game_on=False
            else:
                if full_board_check(board):
                    print('Tie game!')
                    game_on=False
                else:
                    turn='Player 1'
    if not replay():
        break


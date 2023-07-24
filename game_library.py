from ComputerMove import o_wins, x_wins, get_copy_of_board

def print_board(board):
    print(board["tl"] + "|" + board["tm"] + "|" + board["tr"])
    print("-+-+-")
    print(board["ml"] + "|" + board["mm"] + "|" + board["mr"])
    print("-+-+-")
    print(board["bl"] + "|" + board["bm"] + "|" + board["br"])

def get_game_state(board):
    game_state = game_is_over(board)
    if game_state == 'X':
        print('X wins!')
        game_over = True
    elif game_state == 'O':
        print('O wins!')
        game_over = True
    elif game_state == 'Tie':
        print('Cats game!')
        game_over = True
    else:
        print_board(board)
        print('********')

def game_is_over(board):
    if o_wins(board):
        return 'O'
    elif x_wins(board):
        return 'X'
    for key in board:
        if board[key] == 'b':
            return False
    return 'Tie'

def get_move(board):
    """
    Gets move from user, loops on bad input
    Returns:
    str: move
    """
    board = get_copy_of_board(board)
    print("Options are: tl, tm, tr, ml, mm, mr, bl, bm, br")
    while True: # loop until we get a valid move
        move = input("Where would you like to move? ")
        if len(move) == 2 and move[0] in ['t', 'm', 'b'] and move[1] in ['l', 'm', 'r']:
            if board[move] == "b":
                return move
                
            else:
                print("That spot is already taken!")
                print_board(board)
        else:
            print("That is not a valid move!")
            print_board(board)
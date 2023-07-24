from game_library import game_is_over, print_board, get_game_state, get_move
from ComputerMove import get_computer_move
# global vars
game_board = { # start with all blank board
    "tl": "b",
    "tm": "b",
    "tr": "b",
    "ml": "b",
    "mm": "b",
    "mr": "b",
    "bl": "b",
    "bm": "b",
    "br": "b"
}
game_over = False # game is not over 
x_turn = True # x goes

def get_game_state(board):
    """
    Returns game state and prints message if game is over
    Returns:
    bool: True if game is over, False if game is not over
    params:
    board: dict of board state (of the form defined above)
    """
    game_state = game_is_over(board)
    if game_state == 'X':
        print('X wins!')
        return True
    elif game_state == 'O':
        print('O wins!')
        return True
    elif game_state == 'Tie':
        print('Cats game!')
        return True
    else:
        print_board(game_board)
        print('********')
        return False


def game():
    """
    Main game loop
    """
    global game_over, x_turn
    print_board(game_board)

    while not game_over:
        if x_turn:
            move = get_move(game_board) # get move from user
            game_board[move] = "X"
            x_turn = False

        else:  # computer's turn
            move = get_computer_move(game_board)
            game_board[move] = 'O'
            x_turn = True
            game_over = get_game_state(game_board)
    print_board(game_board)
    print('Game Over')
    

game()

from game_library import probability_of_winning, game_is_over, needs_to_block, print_board, get_game_state

# create board
game_board = {
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

game_over = False
def get_game_state(board):
    game_state = game_is_over(game_board)
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

print_board(game_board)
x_turn = True
while not game_over:
    if x_turn:
        print ("Options are: tl, tm, tr, ml, mm, mr, bl, bm, br")
        move = input("Where would you like to move? ")
        if move[0] in ['t', 'm', 'b'] and move[1] in ['l', 'm', 'r']:
            game_board[move] = "X"
            x_turn = False
        else:
            game_over = True
    else: # computer's turn
        # get list of all spots that are blank
        must_block = needs_to_block(game_board)
        if must_block:
            game_board[must_block] = 'O'
            x_turn = True
        else:
            blank_spots = []
            move_probability = {} # key is move, value is probability of winning

            for key in game_board:
                if game_board[key] == 'b': # blank means we COULD move there
                    blank_spots.append(key)

            for b in blank_spots:
                temp_board = {} # create new board to not modify existing
                for key in game_board:
                    if key == b:
                        temp_board[key] = 'O'
                    else:
                        temp_board[key] = game_board[key]
                move_probability[b] = probability_of_winning(temp_board)
                
            # check all moves to see which has highest probability of leading to win state
            optimal_move = ['', 0] # [move, probability]
            for key in move_probability:
                if move_probability[key] >= optimal_move[1]:
                    optimal_move = [key, move_probability[key]]
            game_board[optimal_move[0]] = 'O' # make the move
        x_turn = True
        game_over = get_game_state(game_board)
print_board(game_board)    
print ('Game Over')
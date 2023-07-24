# global variables
lines = []
all_games = []
valid_combos = [  # 8 possible winning combinations
    ['tl', 'tm', 'tr'],
    ['ml', 'mm', 'mr'],
    ['bl', 'bm', 'br'],
    ['tl', 'ml', 'bl'],
    ['tm', 'mm', 'bm'],
    ['tr', 'mr', 'br'],
    ['tl', 'mm', 'br'],
    ['tr', 'mm', 'bl']
]

# main script, generates all possible games
with open('master_game_file.csv', "r") as file:
    lines_w_commas = file.readlines()  # This will read all lines into a list
    for line in lines_w_commas:
        temp_line = ''
        for i in range(len(line)):
            if (line[i] != ','):
                temp_line += line[i]
        lines.append(temp_line)

keys = ['tl', 'tm', 'tr', 'ml', 'mm', 'mr', 'bl', 'bm', 'br']
for line in lines:
    temp_game = {}
    for i in range(len(line)):
        if line[i] == 'x':
            temp_game[keys[i]] = 'X'
        elif line[i] == 'o':
            temp_game[keys[i]] = 'O'
        elif line[i] == 'b':
            temp_game[keys[i]] = 'b'
    all_games.append(temp_game)


# FUNCTIONS
def o_wins(board):
    # check if any of the combos are all 'O'
    for combo in valid_combos:
        if board[combo[0]] == 'O' and board[combo[1]] == 'O' and board[combo[2]] == 'O':
            return True
    return False

def x_wins(board):
    # check if any of the combos are all 'O'
    for combo in valid_combos:
        if board[combo[0]] == 'X' and board[combo[1]] == 'X' and board[combo[2]] == 'X':
            return True
    return False

def possible_outcome(player_board, computer_board):
    for key in player_board:
        if player_board[key] == 'X' and computer_board[key] != 'X':
            return False
        elif player_board[key] == 'O' and computer_board[key] != 'O':
            return False
    return True

def probability_of_winning(player_board):
    valid_games = 0
    win_games = 0
    for game in all_games:
        if possible_outcome(player_board, game):
            valid_games += 1
            if o_wins(game):
                win_games += 1
    if valid_games == 0:
        return 0  # prevent divide by zero
    return win_games/valid_games

def needs_to_block(board): 
    """
    returns a key to block or False
    """
    for combo in valid_combos:
        number_of_x = 0
        for opt in combo:
            if board[opt] == 'X':
                number_of_x += 1
            elif board[opt] == 'O':
                continue  # if we have O in a spot, we dont care about that combo
        if number_of_x == 2:  # this should imply that the third spot is blank
            for opt in combo:
                if board[opt] == 'b':
                    print('blocking ', opt)
                    return opt
    return False

def win_game(board):
    for combo in valid_combos:
        number_of_o = 0
        for opt in combo:
            if board[opt] == 'O':
                number_of_o += 1
            elif board[opt] == 'X':
                continue  # if we have X in a spot, we dont care about that combo
        if number_of_o == 2:  # this should imply that the third spot is blank
            for opt in combo:
                if board[opt] == 'b':
                    print('winning ', opt)
                    return opt
    return False

def get_copy_of_board(board):
    """
    Returns a copy of the board
    Returns:
    dict: copy of board
    """
    copy_board = {}
    for key in board:
        copy_board[key] = board[key]
    return copy_board

def get_computer_move(board):
        """
        Gets move from computer
        Glue for the AI
        """
        board = get_copy_of_board(board)
        winning_move = win_game(board)
        if winning_move:
            return winning_move

        must_block = needs_to_block(board)
        if must_block:
            return must_block
        # get all blank spots to calculate best move from each
        blank_spots = []
        move_probability = {}  # key is move, value is probability of winning

        for key in board:
            if board[key] == 'b':  # blank means we COULD move there
                blank_spots.append(key)

        for b in blank_spots:
            temp_board = {}  # create new board to not modify existing
            for key in board:
                if key == b:
                    temp_board[key] = 'O'
                else:
                    temp_board[key] = board[key]
            move_probability[b] = probability_of_winning(temp_board)

        # check all moves to see which has highest probability of leading to win state
        optimal_move = ['', 0]  # [move, probability]
        for key in move_probability:
            if move_probability[key] >= optimal_move[1]:
                optimal_move = [key, move_probability[key]]
        return optimal_move[0]  # return the move
lines = []  # give global scope to lines
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

def print_board(board):
    print(board["tl"] + "|" + board["tm"] + "|" + board["tr"])
    print("-+-+-")
    print(board["ml"] + "|" + board["mm"] + "|" + board["mr"])
    print("-+-+-")
    print(board["bl"] + "|" + board["bm"] + "|" + board["br"])


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

def game_is_over(board):
    if o_wins(board):
        return 'O'
    elif x_wins(board):
        return 'X'
    for key in board:
        if board[key] == 'b':
            return False
    return 'Tie'

def needs_to_block(board):  # returns a key to block or False
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
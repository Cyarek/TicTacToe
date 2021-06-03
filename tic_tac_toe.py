import random
from sys import platform
from os import system
from time import sleep

def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [[".", ".", "."],[".", ".", "."],[".", ".", "."]]
    return board

def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    check_anwser = True
    possible_moves = {
    "A1": [0, 0], "A2": [0, 1], "A3": [0, 2],
    "B1": [1, 0], "B2": [1, 1], "B3": [1, 2],
    "C1": [2, 0], "C2": [2, 1], "C3": [2, 2],
    }
    possible_board = {
    "A1": board[0][0], "A2": board[0][1], "A3": board[0][2],
    "B1": board[1][0], "B2": board[1][1], "B3": board[1][2],
    "C1": board[2][0],"C2": board[2][1],"C3": board[2][2]    
    }
    while check_anwser == True:
        player_input = input("Please type cordainates: ").upper()
        if player_input == "QUIT":
            exit()
        elif player_input in possible_moves:
            if possible_board.get(player_input) != ".":
                print("Coordinates are incorect, please type tham again...")
            else:
                return possible_moves.get(player_input)

def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    sleep(1.00)
    coordinates_of_posible_moves = []
    for row_coordinate in range(len(board)):
        for col_coordinate in range(len(board[row_coordinate])):
            if board[row_coordinate][col_coordinate] == ".":
                coordinates_of_posible_moves.append([row_coordinate, col_coordinate])
    if player == -1: 
        oponent_player = 1
        oponent_player_mark = "x"
        my_player_mark = "o"
    elif player == 1:
        oponent_player = -1
        oponent_player_mark = "o"
        my_player_mark = "x"
    else: print("An error has occured, player can't be equal 0")
    next_move_board = board.copy()
    for current_posible_move in range(len(coordinates_of_posible_moves)):
        row, col = coordinates_of_posible_moves[current_posible_move]
        next_move_board[row][col] = my_player_mark
        if has_won(next_move_board, player):
            return row, col
        else:
            next_move_board[row][col] = "."
    for current_posible_move in range(len(coordinates_of_posible_moves)):
        row, col = coordinates_of_posible_moves[current_posible_move]
        next_move_board[row][col] = oponent_player_mark
        if has_won(next_move_board, oponent_player):
            return row, col
        else:
            next_move_board[row][col] = "."
    row, col = coordinates_of_posible_moves[random.randrange(0, len(coordinates_of_posible_moves))]
    return row, col

def mark(board, player, row, col):
    active_player = ""
    if player == +1: active_player = "x"
    elif player == -1: active_player = "o"
    else: print("An error has occured, player can't be = 0")
    board[row][col] = active_player #to check
    return board

def has_won(board, player):
    """Returns True if player has won the game."""
    if player == 1:
        active_player = "x"
    elif player == -1:
        active_player = "o"
    win_board = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    if [active_player, active_player, active_player] in win_board:
        return True
    else:
        return False

def is_full(board):
    """Returns True if board is full."""

    board_fill = False
    while board_fill == False:
        for x in range(0, len(board)):
            board_now = board[x]
            for y in range(0, len(board_now)):
                if board_now[y] == '.':
                    return False
                else:
                    pass
        board_fill = True
    return True

def print_board(board):
    board_test = f'''
       1   2   3
    A  {board[0][0]} | {board[0][1]} | {board[0][2]} 
      ---+---+---
    B  {board[1][0]} | {board[1][1]} | {board[1][2]} 
      ---+---+---
    C  {board[2][0]} | {board[2][1]} | {board[2][2]} 

    '''
    print(board_test)
    
def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == +1:
        print("X has won!")
    elif winner == -1:
        print("0 has won!")
    elif winner == 0:
        print("It's Tie")
    else:
        print("An error has occured")

def clear():
    """Clears the consoles"""
    system('cls')

def tictactoe_game(mode):
    board = init_board()
    player_names = mode.split("-")
    game_on = True 
    player = 1
    while game_on:
        clear()
        print_board(board)
        if player == 1:
            if player_names[0] == "HUMAN": row, col = get_move(board, player)
            elif player_names[0] == "AI": row, col = get_ai_move(board, player)
            else: print("An error has occured player_names is not AI noither HUMAN")
        if player == -1:
            if player_names[1] == "HUMAN": row, col = get_move(board, player)
            elif player_names[1] == "AI": row, col = get_ai_move(board, player)
            else: print("An error has occured player_name1&2 shoud be AI or HUMAN")
        board = mark(board, player, row, col)
        if has_won(board, player):
            clear()
            print_board(board)
            print_result(player)
            if input("Do you want to play again? Type \"yes\" if you want so...").upper() == "YES":
                clear()
                main_menu()
            else: exit()
        if is_full(board):
            clear()
            print_board(board)
            print_result(0)
            if input("Do you want to play again? Type \"yes\" if you want so...").upper() == "YES":
                clear()
                main_menu()
            else: exit()
        if player == 1: player = -1
        elif player == -1: player = 1
        else: print("An error has occured")
        
def choose_game_mode():
    mode = False
    while mode == False:
        responses = ['HUMAN-HUMAN', 'HUMAN-AI', 'AI-HUMAN', 'AI-AI' ]
        game_mode = input(' Welcome to Tic-Tac-Toe Game :) \n \n '
        'Please type: "HUMAN-HUMAN" / "HUMAN-AI" / "AI-HUMAN" / "AI-AI", to select game mode: \n \n \t').upper()

        if game_mode in responses:
            return game_mode
        else:
            print('incorrect')

def main_menu():
    tictactoe_game(choose_game_mode())

if __name__ == '__main__':
    main_menu()

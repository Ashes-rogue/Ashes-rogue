import random
import time

def board(b):
    print(f" {b[0][0]} | {b[0][1]} | {b[0][2]} ")
    print("___|___|___")
    print(f" {b[1][0]} | {b[1][1]} | {b[1][2]} ")
    print("___|___|___")
    print(f" {b[2][0]} | {b[2][1]} | {b[2][2]} ")
    print("   |   |   ")

def player_turn(player, b):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (1, 2, 3): ")) - 1
            col = int(input(f"Player {player}, enter the column (1, 2, 3): ")) - 1
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter numbers between 1 and 3.")
                continue
            if b[row][col] == ' ':
                b[row][col] = player
                break
            else:
                print("That spot is already taken.")
        except ValueError:
            print("Invalid input. Please enter numbers between 1 and 3.")

def is_winning_move(b, player, row, col):
    b[row][col] = player
    win = check_win(b, player)
    b[row][col] = ' '
    return win

def computer_turn(b, computer_symbol):
    print("Computer's turn:")
    time.sleep(1)

    for row in range(3):
        for col in range(3):
            if b[row][col] == ' ' and is_winning_move(b, computer_symbol, row, col):
                b[row][col] = computer_symbol
                return

    player_symbol = 'X' if computer_symbol == 'O' else 'O'
    for row in range(3):
        for col in range(3):
            if b[row][col] == ' ' and is_winning_move(b, player_symbol, row, col):
                b[row][col] = computer_symbol
                return

    empty_cells = [(row, col) for row in range(3) for col in range(3) if b[row][col] == ' ']
    row, col = random.choice(empty_cells)
    b[row][col] = computer_symbol

def check_win(b, player):
    for row in range(3):
        if all([b[row][col] == player for col in range(3)]):
            return True
    for col in range(3):
        if all([b[row][col] == player for row in range(3)]):
            return True
    if all([b[i][i] == player for i in range(3)]) or all([b[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_tie(b):
    return all([b[row][col] != ' ' for row in range(3) for col in range(3)])

def play_game():
    b = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    choice = input("Do you want to play against another player or the computer? (player/computer): ").lower()
    player_symbol = input("Choose your symbol (X/O): ").upper()
    computer_symbol = 'O' if player_symbol == 'X' else 'X'
    current_player = 'X'

    while True:
        board(b)
        if check_win(b, 'X'):
            print("Player X wins!")
            break
        if check_win(b, 'O'):
            print("Player O wins!" if choice == "player" else "Computer wins! You lose!")
            break
        if check_tie(b):
            print("It's a tie!")
            break

        if choice == "computer" and current_player == computer_symbol:
            computer_turn(b, computer_symbol)
        else:
            player_turn(current_player, b)

        current_player = 'O' if current_player == 'X' else 'X'

play_game()

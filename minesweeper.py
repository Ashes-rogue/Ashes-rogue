import random
import time

ROWS = 8
COLS = 8
MINES = 10

def create_board():
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    mine_positions = random.sample(range(ROWS * COLS), MINES)
    for pos in mine_positions:
        row, col = divmod(pos, COLS)
        board[row][col] = -1
    return board

def count_adjacent_mines(board):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == -1:
                continue
            mines_count = 0
            for r in range(max(0, row-1), min(row+2, ROWS)):
                for c in range(max(0, col-1), min(col+2, COLS)):
                    if board[r][c] == -1:
                        mines_count += 1
            board[row][col] = mines_count

def print_board(board, revealed):
    print("   " + " ".join(map(str, range(1, COLS + 1))))
    for r in range(ROWS):
        print(f"{r + 1:2} ", end='')
        for c in range(COLS):
            if not revealed[r][c]:
                print('#', end=' ')
            elif board[r][c] == -1:
                print('*', end=' ')
            elif board[r][c] == 0:
                print('.', end=' ')
            else:
                print(board[r][c], end=' ')
        print()

def reveal_cell(board, revealed, row, col):
    if revealed[row][col]:
        return
    to_reveal = [(row, col)]
    while to_reveal:
        r, c = to_reveal.pop()
        if revealed[r][c]:
            continue
        revealed[r][c] = True
        if board[r][c] == 0:
            for nr in range(max(0, r-1), min(r+2, ROWS)):
                for nc in range(max(0, c-1), min(c+2, COLS)):
                    if not revealed[nr][nc] and board[nr][nc] != -1:
                        to_reveal.append((nr, nc))

def all_safe_cells_revealed(board, revealed):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] != -1 and not revealed[row][col]:
                return False
    return True

def display_guide():
    print("Welcome to Minesweeper!")
    time.sleep(1)
    print("Here's a quick guide:")
    time.sleep(1)
    print("# - Unrevealed cell")
    time.sleep(1)
    print(". - Revealed empty cell")
    time.sleep(1)
    print("* - Mine")
    time.sleep(1)
    print("1-8 - Number of cells")
    time.sleep(1)
    print()

def play_game():
    board = create_board()
    count_adjacent_mines(board)
    revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]
    
    while True:
        print()
        print_board(board, revealed)
        row_input = input("\nEnter the row (1-8) or 'q' to quit: ").strip()
        if row_input.lower() == 'q':
            print("Thanks for playing!")
            break
        col_input = input("Enter the column (1-8): ").strip()
        
        try:
            row = int(row_input) - 1
            col = int(col_input) - 1
            if not (0 <= row < ROWS and 0 <= col < COLS):
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid input. Try again.")
            continue
        
        if board[row][col] == -1:
            print("Boom! You hit a mine. Game over.")
            revealed = [[True]*COLS for _ in range(ROWS)]
            print_board(board, revealed)
            print("Game over. Better luck next time!")
            break
        
        reveal_cell(board, revealed, row, col)
        
        if all_safe_cells_revealed(board, revealed):
            revealed = [[True]*COLS for _ in range(ROWS)]
            print_board(board, revealed)
            print("Congratulations! You've cleared the board.")
            break

def main():
    display_guide()
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

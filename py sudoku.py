import random
import time
import csv

print("Hello user may I please have your name?")
time.sleep(1)
name = input("Enter name: ")
time.sleep(1)
print("Nice to meet you",name)
time.sleep(1.5)
def start():
    print("What would you like to do?")
    time.sleep(1)
    print('1. Play Sudoku\n2. Leaderboard\n3. Credits\n4. Sudoku? (know more)')

    return(int(input('')))

def sud():
    if input("Generate sudoku?   (enter y)  ")=='y':
        t_start = time.time()

        def generate_sudoku():
            grid = [[0 for _ in range(9)] for _ in range(9)]
            fill_diagonal_grids(grid)
            solve_sudoku(grid)
            remove_numbers(grid)
            return grid

        def fill_diagonal_grids(grid):
            values = random.sample(range(1, 10), 9)

            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    for k in range(3):
                        for l in range(3):
                            if values:
                                grid[i+k][j+l] = values.pop()

        def solve_sudoku(grid):
            empty_cell = find_empty_cell(grid)
            if not empty_cell:
                return True

            row, col = empty_cell

            for num in random.sample(range(1, 10), 9):
                if is_valid_move(grid, row, col, num):
                    grid[row][col] = num
                    if solve_sudoku(grid):
                        return True
                    grid[row][col] = 0

            return False

        def find_empty_cell(grid):
            for i in range(9):
                for j in range(9):
                    if grid[i][j] == 0:
                        return (i, j)
            return None

        def is_valid_move(grid, row, col, num):
            if num in grid[row]:
                return False

            if num in [grid[i][col] for i in range(9)]:
                return False

            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            if num in [grid[start_row + i][start_col + j] for i in range(3) for j in range(3)]:
                return False

            return True

        def remove_numbers(grid):
            difficulty = 40

            for _ in range(difficulty):
                while True:
                    row, col = random.randint(0, 8), random.randint(0, 8)
                    if grid[row][col] != 0:
                        temp = grid[row][col]
                        grid[row][col] = 0

                        copy_grid = [row[:] for row in grid]
                        if not solve_sudoku(copy_grid):
                            grid[row][col] = temp
                        break

        sudoku_puzzle = generate_sudoku()

        for row in sudoku_puzzle:
            print(' '.join(['_' if cell == 0 else str(cell) for cell in row]))

        if input("Sudoku solved?  (press enter button)  ") == '':
            t_end = time.time()
            score = round(t_end - t_start, 2)
            print("Time taken = ", score)

        f=open('SudokuScore.csv','a', newline='')
        n=csv.writer(f, delimiter='\t')
        n.writerow([name,' - ', score])
        f.close()
    else:
        print('Invalid input ')
        time.sleep(1)
        print('How do you wish to procede ?')
        time.sleep(1)
        sud()

choice=start()
if choice==1:
    sud()

elif choice==2:
    f=open('SudokuScore.csv','r',newline='')
    w=csv.reader(f, delimiter='\t')
    for r in w:
        print(r)
    f.close()

elif choice==3:
    lines = [
        '',
        ' C  R  E  D  I  T  S ',
        '______________________',
        '',
        '',
        'Developed by:  Ashitha  &  Sara ',
        '',
        'Version: 1.0',
        'Date: 16-11-25',
        '',
        'Thanks for using the program!']

    for line in lines:
        print(line)
        time.sleep(1.1)

if choice==4:
    lines=[
            '',
            '  K N O W   Y O U R   S U D O K U   !',
            '___________________________________',
            '',
            '',
            'Sudoku is a popular logic-based puzzle game that has taken the world by storm.',
            'The game is played on a 9x9 grid that is divided into nine 3x3 boxes.',
            'The goal here is to fill in the grid with numbers from 1 to 9 such that,',
            'each row, column and 3x3 box contains all of the numbers from 1 to 9 without any repetition.',
            'Sudoku is a great way to exercise your brain and improve your problem-solving skills.',
            'It requires logical thinking, attention to detail, and patience.',
            'The game can be played by people of all ages and skill levels,',
            'and there are endless variations and levels of difficulty to keep you challenged and engaged.']
    
    for line in lines:
        print(line)
        time.sleep(1.2)

while True:
    print('')
    print('What next ?')
    time.sleep(1)
    print('1. Generate sudoku !\n2. Back to home screen\n3. Quit ;(')
    choice2=int(input(''))

    if choice2==1:
        sud()

    elif choice2==2:
        start()
        
    elif choice2==3:
        time.sleep(1)
        print('Sad to see you go...',
              'Hope you had fun !')
        break
    else:
            print('Invalid choice. Please enter 1, 2, or 3.')

import random

MAP_SIZES = {
    1: (4, 4),
    2: (8, 8),
    3: (16, 16),
    4: (32, 32)
}

map_size = (8, 8)
mine_count = 10

def generate_board(rows, cols, mines):
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    mines_placed = 0

    while mines_placed < mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if board[row][col] != "M":
            board[row][col] = "M"
            mines_placed += 1

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == "M":
                continue
            count = 0
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if 0 <= r < rows and 0 <= c < cols and board[r][c] == "M":
                        count += 1
            board[row][col] = count

    return board

def print_board(board, revealed):
    rows, cols = len(board), len(board[0])
    print("   " + "".join(str(i).rjust(2) for i in range(cols)))
    print("  +" + "--" * cols + "+")
    for row in range(rows):
        print(f"{row:2}|", end=" ")
        for col in range(cols):
            if revealed[row][col]:
                if board[row][col] == "M":
                    print("💣", end=" ")
                elif board[row][col] == 0:
                    print(" ", end=" ")
                else:
                    print(board[row][col], end=" ")
            else:
                print("■", end=" ")
        print("|")
    print("  +" + "--" * cols + "+")

def reveal_cells(board, revealed, row, col):
    rows, cols = len(board), len(board[0])
    if revealed[row][col]:
        return
    revealed[row][col] = True
    if board[row][col] == 0:
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if 0 <= r < rows and 0 <= c < cols:
                    reveal_cells(board, revealed, r, c)


def is_game_won(board, revealed):
    rows, cols = len(board), len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] != "M" and not revealed[row][col]:
                return False
    return True

def play_game():
    global map_size, mine_count
    rows, cols = map_size
    board = generate_board(rows, cols, mine_count)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    game_over = False

    while not game_over:
        print_board(board, revealed)
        try:
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            if row < 0 or row >= rows or col < 0 or col >= cols:
                print("Invalid coordinates! Try again.")
                continue
            if revealed[row][col]:
                print("Cell already revealed! Try again.")
                continue
            if board[row][col] == "M":
                print("💥 You hit a mine! Game over.")
                game_over = True
            else:
                reveal_cells(board, revealed, row, col)
                if is_game_won(board, revealed):
                    print("🎉 You won! Congratulations!")
                    game_over = True
        except ValueError:
            print("Invalid input! Please enter numbers.")


def main_menu():
    global map_size, mine_count
    while True:
        print("\n--- Minesweeper Menu ---")
        print("1. New Game")
        print("2. Change Map Size")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("\n--- Change Map Size ---")
            print("1. 4x4")
            print("2. 8x8")
            print("3. 16x16")
            print("4. 32x32")
            size_choice = input("Select a map size: ")
            if size_choice in ["1", "2", "3", "4"]:
                map_size = MAP_SIZES[int(size_choice)]
                mine_count = map_size[0] * map_size[1]
                print(f"Map size changed to {map_size[0]}x{map_size[1]}.")
            else:
                print("Invalid choice!")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()
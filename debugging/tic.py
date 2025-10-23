#!/usr/bin/python3

def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)


def check_winner(board):
    """Checks whether there is a winner on the board."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def is_full(board):
    """Checks if the board is completely filled."""
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """Main game loop for Tic-Tac-Toe."""
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        print(f"\nPlayer {player}'s turn.")

        # Get valid input from user
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input! Please enter numbers only (0, 1, or 2).")
            continue

        # Check bounds
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid move! Row and column must be 0, 1, or 2.")
            continue

        # Check if cell is free
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Make move
        board[row][col] = player

        # Check if player wins
        if check_winner(board):
            print_board(board)
            print(f"\n🎉 Player {player} wins! 🎉")
            break

        # Check for a tie
        if is_full(board):
            print_board(board)
            print("\nIt's a tie! No more moves left.")
            break

        # Switch player
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()


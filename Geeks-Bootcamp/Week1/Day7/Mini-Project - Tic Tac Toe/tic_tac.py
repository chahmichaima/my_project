board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
def display_board():
    print("\nTIC TAC TOE")
    print("*****************")
    print(f"*   {board[0][0]} | {board[0][1]} | {board[0][2]}   *")
    print("*  ---|---|---  *")
    print(f"*   {board[1][0]} | {board[1][1]} | {board[1][2]}   *")
    print("*  ---|---|---  *")
    print(f"*   {board[2][0]} | {board[2][1]} | {board[2][2]}   *")
    print("*****************\n")
def player_input(player):
    print(f"Player {player}'s turn...")
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if row in [0, 1, 2] and col in [0, 1, 2]:
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("That space is already taken! Choose another one.")
            else:
                print("Invalid input! Please enter numbers between 0 and 2.")
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
def check_win():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None
def play():
    current_player = "X"
    turns = 0
    print("Welcome to TIC TAC TOE!")
    while turns < 9:
        display_board()
        player_input(current_player)
        winner = check_win()
        if winner:
            display_board()
            print(f"Congratulations! Player {winner} wins!")
            return
        current_player = "O" if current_player == "X" else "X"
        turns += 1
    display_board()
    print("It's a tie!")
if __name__ == "__main__":
    play()
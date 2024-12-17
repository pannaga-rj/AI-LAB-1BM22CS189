import math

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
    print()

# Check for a winner
def check_winner(board):
    # Check rows, columns, and diagonals
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

# Check if the board is full
def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':  # Maximizer wins
        return 10 - depth
    elif winner == 'O':  # Minimizer wins
        return depth - 10
    elif is_full(board):  # Tie
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
        return best_score

# Find the best move
def find_best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main function to play Tic Tac Toe
def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe: X (AI) vs O (Player)")
    print_board(board)

    while True:
        # Player's move
        row, col = map(int, input("Enter your move (row and column: 0 1 2): ").split())
        if board[row][col] != ' ':
            print("Cell is already taken. Try again.")
            continue
        board[row][col] = 'O'

        # Check for end of game
        if check_winner(board) or is_full(board):
            break

        # AI's move
        print("AI's turn...")
        move = find_best_move(board)
        if move:
            board[move[0]][move[1]] = 'X'

        # Print the board
        print_board(board)

        # Check for end of game
        if check_winner(board) or is_full(board):
            break

    # Determine the result
    winner = check_winner(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a tie!")
    print_board(board)

if __name__ == "__main__":
    main()

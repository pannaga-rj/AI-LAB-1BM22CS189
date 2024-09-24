import random

# Initialize the game board
d = [["-"] * 3 for _ in range(3)]
turn = {0: [0, 0], 1: [0, 1], 2: [0, 2], 3: [1, 0], 4: [1, 1], 5: [1, 2], 6: [2, 0], 7: [2, 1], 8: [2, 2]}

r0 = [0, 1, 2]
r1 = [3, 4, 5]
r2 = [6, 7, 8]
c0 = [0, 3, 6]
c1 = [1, 4, 7]
c2 = [2, 5, 8]
d1 = [0, 4, 8]  # Diagonal \
d2 = [2, 4, 6]  # Diagonal /

avoid_win_turns = {
    0: [r0, d1, c0],
    1: [r0, c1],
    2: [r0, c2, d2],
    3: [r1, c0],
    4: [d1, d2, c1, r1],
    5: [r1, c2],
    6: [r2, c0, d2],
    7: [r2, c1],
    8: [r2, c2, d1]
}

# Get player symbol
p1 = input("Player enter your symbol (x/o): ").strip().lower()

if p1 == "x":
    p2 = "o"
else:
    p2 = "x"

# Check if a player is about to win
def check_winning_move(symbol):
    for move, lines in avoid_win_turns.items():
        if d[turn[move][0]][turn[move][1]] == "-":  # Only consider available spots
            for line in lines:
                if sum(1 for m in line if d[turn[m][0]][turn[m][1]] == symbol) == 2:
                    return move
    return None

# Player's move
def player_move():
    while True:
        move = int(input("Enter your move (0-8): "))
        if move in turn and d[turn[move][0]][turn[move][1]] == "-":
            d[turn[move][0]][turn[move][1]] = p1
            break
        else:
            print("Invalid move. Try again.")

# Computer's move
def computer_move():

    ''' getting index of empty rows '''
    available_moves = [i for i in range(9) if d[turn[i][0]][turn[i][1]] == "-"]

    if not available_moves:
        return  # No moves available

    # Check if the computer can win
    winning_move = check_winning_move(p2)
    if winning_move is not None:
        d[turn[winning_move][0]][turn[winning_move][1]] = p2
        return

    # Check if the player is about to win and block them
    block_move = check_winning_move(p1)
    if block_move is not None:
        d[turn[block_move][0]][turn[block_move][1]] = p2
        return

    # Otherwise, make a move from the available moves based on avoid_win_turns
    for move in available_moves:
        if move in avoid_win_turns:
            possible_moves = avoid_win_turns[move]
            # Flatten the possible moves and filter by available moves
            filtered_moves = [m for sublist in possible_moves for m in sublist if m in available_moves]
            if filtered_moves:
                computer_choice = random.choice(filtered_moves)
                d[turn[computer_choice][0]][turn[computer_choice][1]] = p2
                return

    # If no strategic move, pick randomly
    random_move = random.choice(available_moves)
    d[turn[random_move][0]][turn[random_move][1]] = p2

# Print the board
def print_board():
    for row in d:
        print(" ".join(row))

# Check if a player has won
def check_winner(symbol):
    return any(row.count(symbol) == 3 for row in d) or \
           any(col.count(symbol) == 3 for col in zip(*d)) or \
           (d[0][0] == d[1][1] == d[2][2] == symbol) or \
           (d[0][2] == d[1][1] == d[2][0] == symbol)

# Game loop
for _ in range(5):  # Maximum of 5 turns (5 moves each)
    print_board()
    player_move()
    if check_winner(p1):
        print_board()
        print("Player wins!")
        break

    if all(d[turn[i][0]][turn[i][1]] != "-" for i in range(9)):
        print_board()
        print("It's a draw!")
        break

    computer_move()
    if check_winner(p2):
        print_board()
        print("Computer wins!")
        break

    ''' if all items are filled with x or o ''' 
    if all(d[turn[i][0]][turn[i][1]] != "-" for i in range(9)):
        print_board()
        print("It's a draw!")
        break

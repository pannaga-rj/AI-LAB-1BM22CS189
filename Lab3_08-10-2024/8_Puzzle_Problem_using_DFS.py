from copy import deepcopy

# Define the goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Function to find the position of the blank tile (0)
def find_blank_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None

# Function to calculate the Manhattan distance
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:  # Ignore the blank tile
                goal_x, goal_y = divmod(tile - 1, 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

# Function to make a move by sliding the blank tile (0)
def make_move(state, move):
    new_state = deepcopy(state)
    blank_x, blank_y = find_blank_tile(state)

    if move == "up" and blank_x > 0:
        new_state[blank_x][blank_y], new_state[blank_x - 1][blank_y] = new_state[blank_x - 1][blank_y], new_state[blank_x][blank_y]
    elif move == "down" and blank_x < 2:
        new_state[blank_x][blank_y], new_state[blank_x + 1][blank_y] = new_state[blank_x + 1][blank_y], new_state[blank_x][blank_y]
    elif move == "left" and blank_y > 0:
        new_state[blank_x][blank_y], new_state[blank_x][blank_y - 1] = new_state[blank_x][blank_y - 1], new_state[blank_x][blank_y]
    elif move == "right" and blank_y < 2:
        new_state[blank_x][blank_y], new_state[blank_x][blank_y + 1] = new_state[blank_x][blank_y + 1], new_state[blank_x][blank_y]

    return new_state

# Function to get valid moves for the blank tile (0)
def get_valid_moves(state):
    blank_x, blank_y = find_blank_tile(state)
    moves = []
    if blank_x > 0:
        moves.append("up")
    if blank_x < 2:
        moves.append("down")
    if blank_y > 0:
        moves.append("left")
    if blank_y < 2:
        moves.append("right")
    return moves

# DFS search function using a stack
def dfs_solve_puzzle(initial_state):
    # Stack for DFS (each entry contains the current state and path of moves)
    stack = [(initial_state, [])]

    # Keep track of visited states
    visited = set()

    while stack:
        current_state, path = stack.pop()

        # Mark the current state as visited (convert the state to a tuple so it's hashable)
        state_tuple = tuple(tuple(row) for row in current_state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        # If the current state is the goal state, return the path of moves
        if current_state == goal_state:
            return path

        # Get all valid moves and generate new states
        valid_moves = get_valid_moves(current_state)
        for move in valid_moves:
            new_state = make_move(current_state, move)
            new_path = path + [move]
            stack.append((new_state, new_path))

    return None  # No solution found

# Main function to start the puzzle game
if __name__ == "__main__":
    # Define the initial state
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]

    # Run DFS to solve the puzzle
    solution_moves = dfs_solve_puzzle(initial_state)

    if solution_moves:
        print("Solution found!")
        print(f"Moves: {' -> '.join(solution_moves)}")
    else:
        print("No solution exists for this puzzle.")

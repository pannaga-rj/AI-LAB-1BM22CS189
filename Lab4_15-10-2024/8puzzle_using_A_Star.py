import heapq
from copy import deepcopy

# Define the goal state
goal_state = [
    [2, 8, 1],
    [0, 4, 3],
    [7, 6, 5]
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


def astar_solve_puzzle(initial_state):
    """Solves the 8-puzzle using A* search with Manhattan distance heuristic."""

    open_list = [(manhattan_distance(initial_state), initial_state, [])]  # (f, state, path)
    closed_list = set()

    while open_list:

        # Extracting last tuple and destructuring into three variables
        _, current_state, path = heapq.heappop(open_list)

        # tuple of tuples
        state_tuple = tuple(map(tuple, current_state))

        # checking
        if current_state == goal_state:
            return path


        # set of tuples
        if state_tuple in closed_list:
            continue
        closed_list.add(state_tuple)

        for move in get_valid_moves(current_state):

            # making moves to all possible places
            new_state = make_move(current_state, move)

            # appending to new path to list
            new_path = path + [move]

            # calculating new distance
            f_value = manhattan_distance(new_state) + len(new_path)  # f = g + h

            # by doing this we get min distance state,  which will be used for next state.
            heapq.heappush(open_list, (f_value, new_state, new_path))

    return None  # No solution found



# Main function
if __name__ == "__main__":
    # ... (your initial state definition) ...
    # Define the initial state
    initial_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    # Run A* search using Manhattan distance
    solution_moves = astar_solve_puzzle(initial_state)

    if solution_moves:
        print("Solution found!")
        print(f"Moves: {' -> '.join(solution_moves)}")
    else:
        # if len(solution_moves) == 0:
        #   print("ALready Won!")
        # else:
          print("No solution exists for this puzzle.")

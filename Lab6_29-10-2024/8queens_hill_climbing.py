## hill climbing
import random

# Define the board state with queens' positions
class State:
    def __init__(self, queens):
        self.queens = queens
        self.h = self.heuristic()  # Calculate initial conflicts (heuristic)

    def heuristic(self):
        """Calculate the number of conflicts."""
        conflicts = 0
        for i in range(len(self.queens)):
            for j in range(i + 1, len(self.queens)):
                # Check for conflicts in same column or diagonals
                if self.queens[i] == self.queens[j] or abs(self.queens[i] - self.queens[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def generate_neighbors(self):
        """Create new board arrangements by moving each queen in its row."""
        neighbors = []
        for row in range(len(self.queens)):
            for col in range(8):  # Try each column for each queen
                if col != self.queens[row]:  # Move only if it's a new position
                    new_queens = self.queens[:]
                    new_queens[row] = col
                    neighbors.append(State(new_queens))
        return neighbors

# Hill climbing to find a solution
def hill_climbing(initial_state):
    current_state = initial_state

    while True:
        neighbors = current_state.generate_neighbors()  # All possible next steps
        next_state = min(neighbors, key=lambda s: s.h)  # Pick neighbor with least conflicts

        if next_state.h >= current_state.h:  # If no better neighbor, stop
            break
        current_state = next_state  # Move to better neighbor

    return current_state  # Return the found state

# Run the hill-climbing algorithm
initial_queens = [random.randint(0, 7) for _ in range(8)]  # Random starting position
initial_state = State(initial_queens)
solution = hill_climbing(initial_state)

# Output the solution
print("Solution found:", solution.queens)
print("Conflicts:", solution.h)

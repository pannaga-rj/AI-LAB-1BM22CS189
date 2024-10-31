import heapq
import numpy as np
# Define the state as the current board configuration
class State:
    def __init__(self, queens):
        self.queens = queens   # List of queen positions in each row
        self.g = len(queens)   # Number of queens placed (cost)
        self.h = self.heuristic()  # Estimated conflicts (heuristic)
   
    def heuristic(self):
        conflicts = 0
        for i in range(len(self.queens)):
            for j in range(i + 1, len(self.queens)):
                # Check for conflicts (same column or diagonal)
                if self.queens[i] == self.queens[j] or abs(self.queens[i] - self.queens[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def f(self):
        return self.g + self.h   # A* cost function f(n) = g(n) + h(n)

    # Define the less-than method for priority queue comparison
    def __lt__(self, other):
        return self.f() < other.f()
   
    def generate_children(self):
        children = []
        row = len(self.queens)
        for col in range(8):   # Try placing queen in each column
            if col not in self.queens:  # Avoid placing in the same column
                new_state = State(self.queens + [col])  # Add queen
                children.append(new_state)
        return children

# A* search for the 8-queens solution
def a_star_search():
    initial_state = State([])  # Start with no queens placed
    open_set = []
    heapq.heappush(open_set, (initial_state.f(), initial_state))
   
    while open_set:
        _, current_state = heapq.heappop(open_set)
       
        # Check if the goal is reached
        if current_state.g == 8 and current_state.h == 0:
            return current_state.queens  # Solution found

        # Generate children and add to open set
        for child in current_state.generate_children():
            heapq.heappush(open_set, (child.f(), child))

    return None  # No solution found

# Run the algorithm
solution = a_star_search()
if solution:
    a = [["-"] * 8 for i in range(8)]
    for r in range(8):
        for c in range(8):
            if c == solution[r]:
                a[r][c] = solution[r]
    print(np.array(a))
    print("Solution found:", solution)
else:
    print("No solution found")

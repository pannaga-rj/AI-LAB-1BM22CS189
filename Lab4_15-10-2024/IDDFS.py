# Define a simple Node class for the tree structure
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

# Iterative Deepening Depth-First Search (IDDFS)
def iddfs(root, goal):
    depth = 0
    while True:
        print(f"Searching at depth {depth}...")
        result = dls(root, goal, depth)
        if result == "found":
            return "Goal State Found"
        depth += 1

# Depth-Limited Search (DLS)
def dls(node, goal, depth):
    if depth == 0:
        if node.value == goal:
            return "found"
        else:
            return "not found"

    elif depth > 0:
        for child in node.children:
            result = dls(child, goal, depth - 1)
            if result == "found":
                return "found"
    return "not found"

# Build the tree (graph)
root = Node('Y')
p = Node('P')
X = Node('X')
r = Node('R')
S = Node('S')
F = Node('F')
H = Node('H')
B = Node('B')
C = Node('C')
Z = Node('Z')
U = Node('U')
E = Node('E')
L = Node('L')
W = Node('W')
x = Node('x')



# Connect the nodes (edges)
root.children = [p, X]
p.children = [r, S]
X.children = [F, H]
r.children = [B, C]

S.children = [x, Z]
p.children = [r, S]
X.children = [F, H]
F.children = [U, E]
H.children = [L, W]


# Define the goal state
goal = 'F'

# Run IDDFS
result = iddfs(root, goal)
print(result)

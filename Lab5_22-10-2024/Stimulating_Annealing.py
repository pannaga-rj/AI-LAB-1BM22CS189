import math
import random

# Simulated Annealing function
def SA(initial_state, initial_temp, cooling_rate, max_iterations):
    stop_rate = 1  # Stop when temperature is low enough
    current_state = initial_state  # Initialize the current state
    current_cost = objective_function(current_state)  # Cost of the current state
    
    best_state = current_state  # Track the best state found
    best_cost = current_cost  # Track the best cost found
    
    temp = initial_temp  # Start with the initial temperature

    # Main loop for Simulated Annealing
    while temp > stop_rate:  # Stop when temperature is lower than the stop rate
        for i in range(max_iterations):  # Iterate for a number of steps at each temperature level
            # Generate a new state by perturbing the current state slightly
            new_state = [x + random.uniform(-1, 1) for x in current_state]
            new_cost = objective_function(new_state)  # Calculate cost of the new state

            # Acceptance probability calculation
            if acceptance_probablity(current_cost, new_cost, temp) > random.random():
                current_state = new_state  # Move to the new state
                current_cost = new_cost  # Update the current cost

            # Update the best state found so far
            if new_cost < best_cost:
                best_state = new_state
                best_cost = new_cost

        # Cool down the temperature
        temp *= cooling_rate  # Reduce the temperature by the cooling rate

    return best_state, best_cost

# Objective function to minimize
def objective_function(state):
    cost = 0
    for x in state:
        cost += x**2   # Cubic function for each element in the state
    return cost

# Acceptance probability calculation
def acceptance_probablity(current_cost, new_cost, temp):
    if new_cost < current_cost:
        return 1  # Always accept if the new cost is better (lower)
    else:
        # Accept worse solutions with a probability depending on temperature
        return math.exp((current_cost - new_cost) / temp)

# Example execution with initial state and parameters
initial_state = [1,2,3, 4, 5]  # Example list of values as the initial state
initial_temp = 1000  # High starting temperature
cooling_rate = 0.99  # Cooling rate
max_iterations = 100  # Maximum iterations at each temperature level

# Run the Simulated Annealing algorithm
best_state, best_cost = SA(initial_state, initial_temp, cooling_rate, max_iterations)

# Output the results
print("Best State Found:", best_state)
print("Best Cost Found:", best_cost)

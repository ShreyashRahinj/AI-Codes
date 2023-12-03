import math
import random

# Objective function: x^2
def objective_function(x):
    return x ** 2

# Simulated Annealing Algorithm
def simulated_annealing(bounds, max_iter, initial_temp, cooling_rate):
    # Initial solution within the bounds
    current_solution = random.uniform(bounds[0], bounds[1])
    current_cost = objective_function(current_solution)

    # Initial best solution
    best_solution = current_solution
    best_cost = current_cost

    # Annealing process
    temperature = initial_temp
    for i in range(max_iter):
        # Generate a new candidate solution within the neighborhood
        new_solution = random.uniform(bounds[0], bounds[1])
        new_cost = objective_function(new_solution)

        # Check if the new solution is better or should be accepted probabilistically
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
            current_solution = new_solution
            current_cost = new_cost

            # Update the best solution if applicable
            if current_cost < best_cost:
                best_solution = current_solution
                best_cost = current_cost

        # Cooling down the temperature
        temperature *= cooling_rate

    return best_solution, best_cost

# Set parameters
bounds = [-5, 5]
max_iterations = 10000
initial_temperature = 100.0
cooling_rate = 0.95

# Apply simulated annealing
best_solution, best_cost = simulated_annealing(bounds, max_iterations, initial_temperature, cooling_rate)

print("Best solution:", best_solution)
print("Best cost:", best_cost)

import random

distance_matrix = [
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]
]


def calculate_total_distance(path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i]][path[i + 1]]
    total_distance += distance_matrix[path[-1]][path[0]]  # Return to the starting city
    return total_distance


def generate_initial_solution(num_cities):
    return random.sample(range(num_cities), num_cities)


def hill_climbing_tsp(num_iterations):
    num_cities = len(distance_matrix)
    current_solution = generate_initial_solution(num_cities)
    current_distance = calculate_total_distance(current_solution)

    for _ in range(num_iterations):
        neighbor_solution = current_solution.copy()
        i, j = random.sample(range(num_cities), 2)
        neighbor_solution[i], neighbor_solution[j] = neighbor_solution[j], neighbor_solution[i]
        neighbor_distance = calculate_total_distance(neighbor_solution)

        if neighbor_distance < current_distance:
            current_solution = neighbor_solution
            current_distance = neighbor_distance

    return current_solution, current_distance


if __name__ == "__main__":
    num_iterations = 10000
    best_solution, best_distance = hill_climbing_tsp(num_iterations)
    print("Best solution:", best_solution)
    print("Total distance:", best_distance)

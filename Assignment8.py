import numpy as np

# Define the environment
num_states = 6
num_actions = 2

# Initialize Q-table
Q = np.zeros((num_states, num_actions))

# Define parameters
alpha = 0.1
gamma = 0.9
epsilon = 0.1
num_episodes = 1000

# Simulate environment
def simulate_environment(state, action):
    # Define transitions based on your environment
    transitions = {
        (0, 0): 1, (0, 1): 2,
        (1, 0): 3, (1, 1): 4,
        (2, 0): 5, (2, 1): 0,
        (3, 0): 0, (3, 1): 4,
        (4, 0): 3, (4, 1): 5,
        (5, 0): 2, (5, 1): 1,
    }
    return transitions[(state, action)]

# Calculate reward
def calculate_reward(state):
    # Define rewards based on your environment
    rewards = {
        0: 1,
        1: 0,
        2: 0,
        3: -1,
        4: 0,
        5: 0,
    }
    return rewards[state]
# Q-learning algorithm
for episode in range(num_episodes):
    state = 0  # Initial state
    done = False
    while not done:
        # Exploration-exploitation trade-off
        if np.random.uniform(0, 1) < epsilon:
            action = np.random.choice(num_actions)  # Explore
        else:
            action = np.argmax(Q[state, :])  # Exploit
        # Simulate the environment and get the next state and reward
        next_state = simulate_environment(state, action)
        reward = calculate_reward(next_state)
        # Q-learning update rule
        Q[state, action] = (1 - alpha) * Q[state, action] + alpha * (reward + gamma * np.max(Q[next_state, :]))
        state = next_state
        # Check if the episode is done
        if state == 3:  # Goal state
            done = True

# Print the learned Q-table
print("Learned Q-table:")
print(Q)

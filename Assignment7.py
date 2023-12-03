import random

# Function to simulate the Monty Hall problem
def monty_hall_simulation(num_trials):
    switch_wins = 0
    stay_wins = 0

    for _ in range(num_trials):
        # Assign a random location for the prize
        prize_location = random.randint(1, 3)

        # Contestant's initial choice
        contestant_choice = random.randint(1, 3)

        # Host reveals a door that doesn't contain the prize and isn't the contestant's choice
        doors = [1, 2, 3]
        doors.remove(prize_location)
        if contestant_choice in doors:
            doors.remove(contestant_choice)
        host_reveal = random.choice(doors)

        # Determine the remaining door after the host's reveal
        remaining_door = 6 - (contestant_choice + host_reveal)

        # Check if the contestant switches or stays with their initial choice
        if remaining_door == prize_location:
            switch_wins += 1
        if contestant_choice == prize_location:
            stay_wins += 1

    switch_win_percentage = (switch_wins / num_trials) * 100
    stay_win_percentage = (stay_wins / num_trials) * 100

    return switch_win_percentage, stay_win_percentage

# Run the simulation with a large number of trials
num_simulations = 10000
switch_percentage, stay_percentage = monty_hall_simulation(num_simulations)

print(f"Probability of winning by switching doors: {switch_percentage:.2f}%")
print(f"Probability of winning by staying with the initial choice: {stay_percentage:.2f}%")

import itertools
import numpy as np

# Define the rank thresholds
ranks = {
    "Noob": 0,
    "Script Kiddie": 5,
    "Hacker": 20,
    "Pro Hacker": 45,
    "Elite Hacker": 70,
    "Guru": 90,
    "Omniscient": 100
}

# Ask the user for their current stats
current_rank = input("Enter your current rank: ")
ownership_percentage = float(input("Enter your current ownership percentage (xx.xx): "))
active_machines = int(input("Enter the total number of active machines: "))
active_challenges = int(input("Enter the total number of active challenges: "))

print(f"Your current ownership percentage is {ownership_percentage}%")

# Find the next rank
next_rank = None
for rank, threshold in ranks.items():
    if threshold > ownership_percentage:
        next_rank = rank
        next_threshold = threshold
        break

if next_rank is None:
    print("Congratulations, you're Omniscient!")
else:
    print(f"Your next rank is {next_rank}, which requires an ownership percentage of {next_threshold}%.")

    # Estimate the number of system owns and challenge owns needed to reach the next rank
    remaining_percentage = next_threshold - ownership_percentage
    remaining_system_owns = remaining_percentage * (active_machines + (active_machines / 2) + (active_challenges / 10)) / 100

    # Create a list of possible system owns and challenge owns
    possible_system_owns = list(range(min(active_machines, int(remaining_system_owns) + 1)))
    possible_challenge_owns = list(range(min(active_challenges, int(remaining_system_owns * 10) + 1)))

    # Create a list of all combinations of possible system owns and challenge owns
    combinations = list(itertools.product(possible_system_owns, possible_challenge_owns))

    # Calculate the ownership percentage for each combination
    ownership_percentages = [(system_owns + (challenge_owns / 10)) / (active_machines + (active_machines / 2) + (active_challenges / 10)) * 100 for system_owns, challenge_owns in combinations]

    # Find the combinations that get you closest to the next rank
    closest_combinations = sorted(zip(combinations, ownership_percentages), key=lambda x: abs(remaining_percentage - x[1]))

    # Print the best three combinations
    for i in range(min(3, len(closest_combinations))):
        print(f"Combination {i + 1}: {closest_combinations[i][0][0]} system owns and {closest_combinations[i][0][1]} challenge owns")

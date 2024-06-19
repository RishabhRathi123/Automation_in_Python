import random

def roll_fair_die():
    """Simulate rolling a fair 6-sided die."""
    return random.randint(1, 6)

def roll_unfair_die(probabilities):
    """Simulate rolling an unfair 6-sided die."""
    faces = [1, 2, 3, 4, 5, 6]
    return random.choices(faces, weights=probabilities, k=1)[0]

# Example usage
fair_rolls = [roll_fair_die() for _ in range(10)]
print("Fair rolls:", fair_rolls)

# Define the probabilities for an unfair die
# These probabilities should sum to 1
unfair_probabilities = [0.1, 0.2, 0.1, 0.1, 0.2, 0.3]
unfair_rolls = [roll_unfair_die(unfair_probabilities) for _ in range(10)]
print("Unfair rolls:", unfair_rolls)

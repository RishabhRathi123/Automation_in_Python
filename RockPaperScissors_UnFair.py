import random

def get_user_choice():
    """Get the user's choice."""
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice

def get_unfair_computer_choice(user_choice):
    """
    Get the computer's choice in an unfair manner.
    The computer will have higher chances of picking the winning choice against the user.
    """
    choices = ['rock', 'paper', 'scissors']
    weights = [0.33, 0.33, 0.34]  # Default equal probabilities

    if user_choice == 'rock':
        weights = [0.1, 0.6, 0.3]  # Higher chance of picking paper (computer wins)
    elif user_choice == 'paper':
        weights = [0.3, 0.1, 0.6]  # Higher chance of picking scissors (computer wins)
    elif user_choice == 'scissors':
        weights = [0.6, 0.3, 0.1]  # Higher chance of picking rock (computer wins)

    return random.choices(choices, weights=weights, k=1)[0]

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Play a round of Rock-Paper-Scissors."""
    user_choice = get_user_choice()
    computer_choice = get_unfair_computer_choice(user_choice)
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Play the game
if __name__ == "__main__":
    play_game()

import random

def get_user_choice():
    """Prompt the user to choose rock, paper, or scissors."""
    while True:
        user_input = input("\nChoose rock, paper, or scissors (or 'q' to quit): ").lower()
        if user_input in ['rock', 'paper', 'scissors', 'r', 'p', 's', 'q']:
            if user_input == 'r':
                return 'rock'
            elif user_input == 'p':
                return 'paper'
            elif user_input == 's':
                return 'scissors'
            elif user_input == 'q':
                return 'quit'
            else:
                return user_input
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the game rules."""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, result, scores):
    """Display the game results and current scores."""
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    
    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        print("You win!")
    else:
        print("Computer wins!")
    
    print(f"\nCurrent Scores - You: {scores['user']} | Computer: {scores['computer']} | Ties: {scores['tie']}")

def play_game():
    """Main function to run the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors!")
    print("Rules:")
    print("- Rock beats scissors")
    print("- Scissors beat paper")
    print("- Paper beats rock")
    
    scores = {'user': 0, 'computer': 0, 'tie': 0}
    
    while True:
        user_choice = get_user_choice()
        
        if user_choice == 'quit':
            print("\nThanks for playing! Final scores:")
            print(f"You: {scores['user']} | Computer: {scores['computer']} | Ties: {scores['tie']}")
            break
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        # Update scores
        if result == 'tie':
            scores['tie'] += 1
        elif result == 'user':
            scores['user'] += 1
        else:
            scores['computer'] += 1
        
        display_result(user_choice, computer_choice, result, scores)

if __name__ == "__main__":
    play_game()

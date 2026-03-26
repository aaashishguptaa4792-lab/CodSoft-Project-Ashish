import random

def get_computer_choice():
    """Generates a random selection for the computer[cite: 44, 57]."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    """
    Uses a dictionary to map what each choice beats.
    This is cleaner than using 10 different if-statements.
    """
    if user == computer:
        return "tie"
    
    # Logic: Key beats Value
    win_rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if win_rules[user] == computer:
        return "user"
    else:
        return "computer"

def start_game():
    # Score Tracking as requested in Task 4 
    scores = {"user": 0, "computer": 0}
    
    print("=== CODSOFT GAME ARENA ===")
    print("Rules: Rock > Scissors, Scissors > Paper, Paper > Rock [cite: 60]")

    while True:
        # User Input with basic validation [cite: 56]
        user_move = input("\nEnter Rock, Paper, or Scissors (or 'exit' to quit): ").lower()
        
        if user_move == 'exit':
            break
        if user_move not in ['rock', 'paper', 'scissors']:
            print("Invalid move! Please try again.")
            continue

        comp_move = get_computer_choice()
        result = determine_winner(user_move, comp_move)

        # Display Choices and Results [cite: 60, 61]
        print(f"-> You played: {user_move.capitalize()}")
        print(f"-> Computer played: {comp_move.capitalize()}")

        if result == "tie":
            print("🏁 It's a draw!")
        elif result == "user":
            print("🏆 You won this round!")
            scores["user"] += 1
        else:
            print("💻 Computer wins this round!")
            scores["computer"] += 1

        print(f"Current Standings: User {scores['user']} | Computer {scores['computer']}")

        # Play Again prompt [cite: 63]
        if input("\nPlay another round? (y/n): ").lower() != 'y':
            print(f"\nFinal Score - User: {scores['user']} | Computer: {scores['computer']}")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    start_game()

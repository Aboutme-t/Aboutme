import random

def get_user_choice():
    user_choice = input("Choose Rock (r), Paper (p), or Scissors (s): ").lower()
    while user_choice not in ['r', 'p', 's']:
        print("Invalid choice. Please choose Rock (r), Paper (p), or Scissors (s).")
        user_choice = input("Choose again: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['r', 'p', 's'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    for _ in range(10):
        print("\nRound", _ + 1)
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "tie" not in result:
            computer_score += 1

    print("\nGame Over!")
    print("Your score:", user_score)
    print("Computer's score:", computer_score)


    play_game()

import random

NUM_ROUNDS = 5 # Total number of rounds to be played

"""
This program will generate two random numbers from 1 to 100
One is inclusive to user and the other one to the computer
User can see their number but not the computer, thus user have to guess
If user guess correctly, they gain one point
Point will accumulate and display after every single round
After finish 5 rounds, the program will end and display final message

"""
def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Initialize scores
    user_score = 0
    computer_score = 0

    # Loop through each round
    for round_num in range(1, NUM_ROUNDS + 1):
        print() # Blank line before each round for formatting
        print(f"Round {round_num}")

        # Play a single round and get the winner
        winner = user_play_round()

        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        # Show current user score
        print(f"Your score is now {user_score}")

    # End of game messages
    print("Thanks for playing!")
    print("...\n")
    print(f"Your score is now {user_score}\n")
    print_final_message(user_score)

def print_final_message(score):
    """
    Prints a final message based on the user's score at the end of the game
    """

    if score == 5:
        print("Wow! You played perfectly")
    elif score == 2:
        print("Good job, you played really well")
    elif score <= 1:
        print("Better luck next time")

def user_play_round():
    """
    Plays one round of game, then return either "user" or "computer"
    Generates random numbers for user and computers.
    Asks the user to guess whether their number is higher or lower.
    Returns "users" if the user guessed correctly, otherwise "computer".
    """

    # Generate random numbers
    computer_number = random.randint(1, 100)
    user_number = random.randint(1, 100)

    # Show user's number (but not computer's yet)
    print(f"The computer's number is {computer_number}")
    print(f"Your number is {user_number}")

    # Get user's guess input
    guess = get_user_input()

    # If numbers are equal, computer wins the round
    # We called this Edge case
    if user_number == computer_number:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        return "computer"

    # Determine if user's guess was correct
    is_user_correct = (
            (guess == "Lower" and user_number < computer_number ) or
            (guess == "Higher" and user_number > computer_number )
        )
    # Return result based on correctness
    if is_user_correct:
        print(f"You were right! The computer's number was {computer_number}")
        return "user"
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        return "computer"

def get_user_input():
    """
    Safely gets and validates the user's input.
    Keep asking until the user types either 'Higher' or 'Lower'.
    Returns the capitalized valid input.
    """
    guess = input("Do you think your number is higher or lower than the computer's?: ").strip().capitalize()
    while guess not in ["Higher", "Lower"]:
        guess = input("Please enter either Higher or Lower: ").strip().capitalize()
    return guess

# Run the game
if __name__ == "__main__":
    main()

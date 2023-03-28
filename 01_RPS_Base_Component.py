import random


# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0"
        if response != "":

            # If infinite mode not chosen, check response
            # is an integer that is more than 0
            try:
                response = int(response)

                # If response is too low, go back to
                # start of loop
                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

            # If response is not an integer go back to start of loop
        return response


def choice_checker(question, valid_list, error):
    while True:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        for item in valid_list:
            if response == item or response == item[0]:
                return item

        print(error)
        print()


# Main routine goes here

# List of valid response
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have playing before.
# If 'yes', show instructions


# Ask user for # of rounds then loop...
rounds_played = 0

rounds_lost = 0
rounds_drawn = 0
choose_instruction = "Please choose rock (r), paper (p), or scissors (s)"

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start Of Game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = f"Continuous Mode: Round {rounds_played + 1}"
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)
    choose_instruction = "Please choose from rock (r), paper (p), scissors (s)"
    choose_error = "Please choose from rock (r) / paper (p) / scissors (s) / (or xxx to quit)"

    # Ask user for choice and check it's valid
    user_choice = choice_checker(choose_instruction, rps_list, choose_error)

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])

    # Compare choices...
    if comp_choice == user_choice:
        result = "tied"
        rounds_drawn += 1
    elif comp_choice == "rock" and user_choice == "scissors":
        result = "lost"
    elif comp_choice == "paper" and user_choice == "rock":
        result = "lost"
    elif comp_choice == "scissors" and user_choice == "paper":
        result = "lost"
    else:
        result = "won"

    if result == "lost":
        rounds_lost += 1

    if result == "tied":
        feedback = "It's a tie"
    else:
        feedback = f"{user_choice} vs {comp_choice} - you {result}"

    print(f"You chose {user_choice}, the computer chose {comp_choice}. \nResult: {result}")
    print()

    # End game if exit code is typed
    if user_choice == "xxx":
        break

    rounds_played += 1

    if rounds_played == rounds:
        break

# **** rest of the loop / game ****

# Ask user if they want to see their game history.
# If 'yes' show game history

# Show game instructions

# Quick Calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# End of Game Statements (\t means <tab>)
print()
print('***** End Game Summary *****')
print(f"Won: {rounds_won} \t|\t Lost: {rounds_lost} \t|\t Draw: {rounds_drawn}")
print()
print("Thanks for playing")

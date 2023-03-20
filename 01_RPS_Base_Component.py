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


# Main routine goes here

# List of valid response
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have playing before.
# If 'yes', show instructions


# Ask user for # of rounds then loop...
rounds_played = 0
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
    choose = input(f"{choose_instruction} or 'xxx' to end: ")

    # End game if exit code is typed
    if choose == "xxx":
        break

    # **** rest of the loop / game ****

    print("Thank you for playing")

# Ask user if they want to see their game history.
# If 'yes' show game history

# Show game instructions

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


# Ask user if they want to see their game history.
# If 'yes' show game history

# Show game instructions

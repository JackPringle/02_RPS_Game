import random


# Functions go here

# Checks round input is a valid response
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


# Checks user choice of RPS
def choice_checker(question, valid_list, error):
    while True:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        for item in valid_list:
            if response == item or response == item[0]:
                return item

        print(error)
        print()


# checks users enter yes / no to a given question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes / no")


# displays instructions, returns ""
def instructions():
    print("**** How to PLay ****")
    print("-------------------------------------------------------------------")
    print("First, enter the amount of rounds of RPS you want to play.")
    print("For each round, enter either Rock (r), Paper (p), or Scissors (s).")
    print("You will be playing against the computer!")
    print("After you have played all the rounds you requested, you will see your game summary and statistics. ")
    print("Good luck player!")
    print("-------------------------------------------------------------------")
    print()
    return ""


# Main routine goes here

# Welcome user to game
print("---------------------------------------------------------")
print("***** WELCOME TO R/P/S GAME BY FAVOURITE STUDENT *****")
print("---------------------------------------------------------")
print()

# Ask user if they want instructions
played_before = yes_no("Have you played the game before? ")
print()

if played_before == "no":
    instructions()

# List of valid response
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have playing before.
# If 'yes', show instructions


# Ask user for # of rounds then loop...
game_summary = []

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

    print(feedback)
    outcome = f'Round {rounds_played + 1}: {feedback}'
    game_summary.append(outcome)

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

# ***** Calculate Game Stats *****
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100

print()
print("******** Game History ********")
for game in game_summary:
    print(game)

print()

# display game stats with % values to the nearest whole number
print("******** Game Statistics ********")
print(f"Win: {rounds_won}, ({percent_win:.0f}%)\nLoss: {rounds_lost}, ({percent_lose:.0f}%)\nTie: {rounds_drawn}, "
      f"({percent_tie:.0f}%)")


# Thanks user for playing
print("-------------------------------------------------------------------")
print("***** THANKYOU FOR PLAYING R/P/S GAME BY FAVOURITE STUDENT *****")
print("-------------------------------------------------------------------")
print("I know you're impressed miss ;)")
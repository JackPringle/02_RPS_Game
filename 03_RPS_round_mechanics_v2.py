# Function used to check input is valid


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Main Routine goes here...

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
        heading = "Continuous Mode: " \
                  f"Round {rounds_played + 1}"
    else:
        heading = "Round {} of " \
                  f"{rounds_played + 1, rounds}"

    print(heading)
    choose = input(f"{choose_instruction} or 'xxx' to end: ")

    # End game if exit code is typed
    if choose == "xxx":
        break

    # **** rest of the loop / game ****

    print("Thank you for playing")

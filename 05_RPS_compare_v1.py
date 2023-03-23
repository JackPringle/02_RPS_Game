# RPS Component 3 - Compare user choice and computer choice
rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # Compare options...

        if comp_choice == user_choice:
            result = "tie"
        elif comp_choice == "rock" and user_choice == "scissors":
            result = "lose"
        elif comp_choice == "paper" and user_choice == "rock":
            result = "lose"
        elif comp_choice == "scissors" and user_choice == "paper":
            result = "lose"
        else:
            result = "win"

        print(f"You chose {user_choice}, the computer chose {comp_choice}. \nResult: {result}")
        print()

    comp_index += 1
    print()


import random

exit = False
user_points = 0
computer_points = 0

while not exit:  
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game ended")
        print(f"You won a total score of {user_points} and the computer's total score is {computer_points}")
        exit = True

    elif user_input == "rock":
        print("Your input is rock")
        print(f"Computer input is {computer_input}")

        if computer_input == "rock":
            print("It's a tie!")
        elif computer_input == "paper":
            print("Computer wins!")
            computer_points += 1
        elif computer_input == "scissors":
            print("You win!")
            user_points += 1

    elif user_input == "paper":
        print("Your input is paper")
        print(f"Computer input is {computer_input}")

        if computer_input == "rock":
            print("You win!")
            user_points += 1
        elif computer_input == "paper":
            print("It's a tie!")
        elif computer_input == "scissors":
            print("Computer wins!")
            computer_points += 1

    elif user_input == "scissors":
        print("Your input is scissors")
        print(f"Computer input is {computer_input}")

        if computer_input == "rock":
            print("Computer wins!")
            computer_points += 1
        elif computer_input == "paper":
            print("You win!")
            user_points += 1
        elif computer_input == "scissors":
            print("It's a tie!")

    else:
        print("Invalid input. Please choose rock, paper, or scissors.")

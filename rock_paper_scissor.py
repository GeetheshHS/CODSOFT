import random

user_score=0
computer_score=0

choices=['rock','paper','scissor']

while(True):
    print("Choose either rock,paper or scissor")
    user_choice = input("Your choice:").lower()

    if user_choice not in choices:
        print("Invalid choice")
        continue

    computer_choice = random.choice(choices)

    print(f"You choose:{user_choice}")
    print(f"Computer choose:{computer_choice}")

    if user_choice == computer_choice:
        print('Its a tie')
    elif(
        (user_choice == 'rock' and computer_choice =='scissors')or
        (user_choice == 'paper' and computer_choice == 'rock')or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("you won this round")
        user_score=user_score+1
    else:
        print("Computer won this round")
    computer_score=computer_score+1

    print(f"Your score is:{user_score} and the computer score is:{computer_score}")

    again=input("Do you want to play another round?")
    if again == "no":
        print("Thanks for playing")
        print(f"Your score is:{user_score} and the computer_score is:{computer_score}")
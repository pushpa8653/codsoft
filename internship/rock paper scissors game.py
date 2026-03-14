import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("===== Welcome to Rock Paper Scissors =====")
print("Choose one: rock, paper, or scissors")

while True:

    user = input("\nEnter your choice: ").lower()

    if user not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    computer = random.choice(choices)

    print("Your choice:", user)
    print("Computer choice:", computer)

    # Game result
    if user == computer:
        print("It's a Tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    # Show score
    print("\nCurrent Score")
    print("You:", user_score)
    print("Computer:", computer_score)

    # Ask to play again
    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        break


print("\n===== Game Over =====")
print("Final Score")
print("You:", user_score)
print("Computer:", computer_score)

print("\nThank you for playing! 😊")

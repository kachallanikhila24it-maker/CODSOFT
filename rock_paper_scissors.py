import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    user = input("\nEnter rock, paper, or scissors: ").lower()

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

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

    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        break

print("\nFinal Score")
print(f"You: {user_score} | Computer: {computer_score}")
print("Thanks for playing!")

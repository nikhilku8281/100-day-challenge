import random

rock="Rock"
scissor="Scissor"
paper="Paper"
user_choice=int(input("What do You choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_choice=random.randint(0,2)
print(f" Computer choice {computer_choice}")
if user_choice==2 and computer_choice==0:
    print("\nUser Wins")
elif user_choice < computer_choice:
    print("\nComputer wins")
else:
    print("Its a draw")

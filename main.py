import random
print("Welcome to the rock paper and scissors game!")
user = int(input("choose a no. 0 for Rock, 1 for Paper"
          " or 2 for Scissors: "))
computer = random.randint(0 , 2)
print(f"Computer chose {computer}")
if user > 2 or user < 0:
    print("You entered invalid number. YOU LOSE!")
elif user == 0 and computer == 2:
    print("you win!")
elif user == 2 and computer == 0:
    print("you lose!")
elif computer > user:
    print("you lose!")
elif user > computer:
    print("you win!")
elif computer == user:
    print("DRAW!")
else:
    print("LOSER")

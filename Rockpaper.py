import random
user_choice = int(input("Enter your choice:Type 0 for Rock, 1 for paper, 2 for scissors"))
if user_choice >= 3:
    print("Invalid Input!")
else:

    print("You chose:")
if(user_choice == 0):
    print("Rock")
if(user_choice == 1):
    print("Paper")
if(user_choice == 2):
    print("Scissor")
computer_choice = random.randint(0,2)
print("Computer chose:")
if(computer_choice == 0):
    print("Rock")
if(computer_choice == 1):
    print("Paper")
if(computer_choice == 2):
    print("Scissor")
if computer_choice == user_choice:
    print("(Same)It's a draw.")
elif computer_choice == 0 and user_choice == 2:
    print("(Rock)'You loose.'")
elif user_choice == 0 and computer_choice == 2:
    print("(Scissors)'You win.'")
elif computer_choice > user_choice:
    print("You loose")
elif computer_choice < user_choice:
    print("You win.")

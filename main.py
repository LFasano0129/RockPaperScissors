import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# list to store choices
game_signs = [rock, paper, scissors]
# input for player choice
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors: "))
# random function for computer choice
comp_choice = random.randint(0, 2)
# if and elif statements to display results
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_signs[user_choice])
    print(f"Computer chose:\n {game_signs[comp_choice]}")
    if user_choice == 0 and comp_choice == 2:
        print("You win!")
    elif comp_choice == 0 and user_choice == 2:
        print("You lose!")
    elif comp_choice > user_choice:
        print("You lose!")
    elif user_choice > comp_choice:
        print("You win!")
    elif user_choice == comp_choice:
        print("It's a draw")
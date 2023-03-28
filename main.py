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
sign = [rock, paper, scissors]
# input for player choice
choice = input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors: ")
choice_int = int(choice)
# random function for computer choice
comp_choice = random.randint(0, 2)
comp_choice_int = int(comp_choice)
# print statements for displaying choices
print(f"Your chose:\n {sign[choice_int]}\n")
print(f"The computer chose:\n {sign[comp_choice_int]}")
# if and elif statements to display results
if choice_int == 0:
    if comp_choice_int == 0:
        print("Draw")
    elif comp_choice_int == 1:
        print("You Lose!")
    elif comp_choice_int == 2:
        print("You Win!")
elif choice_int == 1:
    if comp_choice_int == 0:
        print("You Win!")
    elif comp_choice_int == 1:
        print("Draw")
    elif comp_choice_int == 2:
        print("You Lose!")
elif choice_int == 2:
    if comp_choice_int == 0:
        print("You Lose!")
    elif comp_choice_int == 1:
        print("You Win!")
    elif comp_choice_int == 2:
        print("Draw")

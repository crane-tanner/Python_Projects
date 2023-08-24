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

r_p_s = [rock, paper, scissors]
length = len(r_p_s)
computer_choice = random.randint(0, length - 1)
print("Welcome to rock, paper, scissors game!")
player_choice = int(input("Choose 0 for rock, 1 for paper, and 2 for scissors. \n"))


if player_choice == 0:
    print(rock)
    print(r_p_s[computer_choice])
    if player_choice == computer_choice:
      print("It's a draw!")
    elif computer_choice == 1:
      print("Paper beats rock. You lose!")
    else:
      print("Rock beats scissors. You win!")

if player_choice == 1:
    print(paper)
    print( r_p_s[computer_choice])
    if player_choice == computer_choice:
      print("It's a draw!")
    elif computer_choice == 0:
      print("Paper b)eats rock. You win!")
    else:
      print("Scissors beats paper. You lose!")

if player_choice == 2:
    print(scissors)
    print(r_p_s[computer_choice])
    if player_choice == computer_choice:
      print("It's a draw!")
    elif computer_choice == 1:
      print("Scissors beats paper. You win!")
    else:
      print("Rock beats scissors. You lose!")
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
rock_paper = [rock, paper, scissors]

your_pick = int(input("What do you choose: Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if your_pick >= 0 and your_pick <=2:   #This is to check that the user makes a valid choice and kind of boundary to what is accepted.
    print(rock_paper[your_pick])
#your_rock_choice = rock_paper[your_pick]

computer_pick = random.randint(0, 2)
#computer_pick = rock_paper[random_pick]
print("Computer chose:")
print(rock_paper[computer_pick])

if your_pick >= 3 or your_pick < 0:
    print("Invalid input. You lose!")
elif your_pick == 0 and computer_pick == 2:
    print("You win!")
elif computer_pick == 0 and your_pick == 2:
    print("You lose!")
elif your_pick > computer_pick:
    print("You win!")
elif computer_pick > your_pick:
    print("You lose!")
elif your_pick == computer_pick:
    print("It's a draw!")



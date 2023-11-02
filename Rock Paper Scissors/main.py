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

#list of rock paper scissors
rps = [rock, paper, scissors]

game = True
score = 0
while game:
    #User choice:
    inp = int(input("Choose 0 for Rock, 1 for Paper, and 2 for Scissors: "))
    print(f"You chose: {rps[inp]}")

    #computer's random choice:
    cmp = random.choice(rps)
    print(f"Computer chose: {cmp}")

    if rps[inp] > cmp:
        score += 1
        print(f"You Win.\nScore is {score}")
    elif rps[inp] == cmp:
        print(f"This is a draw\nScore is {score}")
    else:
        print(f"You Lose\nScore is {score}")

    #asking for another round reeply with yes or no
    i = input("Would you like to play another round: ")
    if i.lower() == "no":
        game = False
    else:
        game = True

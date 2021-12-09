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

#Write your code below this line 👇
number = int(input("What do you choose? Type 0 to choose rock, 1 for paper, 2 for Scissor : "))

if number < 2:
  map = [rock,paper,scissors]
  print(map[number])

  print("computer chose : \n")
  computer_number = random.randint(0,2)
  print(map[computer_number])
  
  if number == computer_number:
    print("match draw")
  elif number == 0 and computer_number == 2:
    print("You win")
  elif number == 0 and computer_number == 1:
    print("You lose")
  elif number == 1 and computer_number == 0:
    print("You win")
  elif number == 1 and computer_number == 2:
    print("you lose")
  elif number == 2 and computer_number == 0:
    print("You lose")
  elif number == 2 and computer_number == 1:
    print("You win")


else:
  print("You entered invalid number\n You lose Game Over")

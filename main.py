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

#Write your code below this line 
import random
print("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.")
enter = int(input("Type you number\n"))
comp = random.randint(0,2)
print(comp,enter)
if enter > 2:
  print("Wrong choice")
else:
  if (comp== 0 and enter == 2) or (comp==1 and enter == 0) or (comp == 2 and enter == 1):
    print("Computer wins, Therefore You lose")
  elif comp == enter:
    print("It is a draw")
  else:
    print("You are the winner!!")
    


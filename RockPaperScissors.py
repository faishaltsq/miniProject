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

user = int(input("what do you choose? type 0 for rock, 1 for paper, 2 for scissors\n"))
computer = random.randint(0,2)  
if user == 0:
    print(rock)
elif user == 1:
    print(paper)
else:
    print(scissors)
    
    
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)
    
if computer == 0:
    if user == 0:
        print("draw")
    elif user == 1:
        print("you win")
    else:
        print("you lose")
elif computer == 1:
    if user == 0:
        print("you lose")
    elif user == 1:
        print("draw")
      
    else:
        print("you win")
else:
    if user == 0:
        print("you win")
    elif user == 1:
        print("you lose")
    else:
        print("draw")

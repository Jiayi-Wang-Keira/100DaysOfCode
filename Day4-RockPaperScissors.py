def print_pattern(choice):
    if choice == 0:
        print('''
        _______
    ---'   ____)  
          (_____)  
          (_____)  
          (____)
    ---.__(___)  
        ''')
    elif choice == 1:
        print('''
        _______
    ---'   ____)____  
              ______)  
              _______)  
             _______)
    ---.__________) 
        ''')
    else:
        print('''
        _______
    ---'   ____)____  
              ______)  
           __________)  
          (____)
    ---.__(___) 
        ''')

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
print_pattern(your_choice)

import random
com_choice = random.randint(0,2)
print("Computer chose:")
print_pattern(com_choice)

if com_choice == your_choice:
    print("Even")
elif (com_choice==0 and your_choice==1) or (com_choice==1 and your_choice==2) or (com_choice==2 and your_choice==0):
    print("You win!")
else:
    print("You lose.")
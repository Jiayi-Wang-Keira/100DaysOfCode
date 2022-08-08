#setup
logo='''

    _   __                __                 ______                     _            
   / | / /_  ______ ___  / /_  ___  _____   / ____/_  _____  __________(_)___  ____ _
  /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/  / / __/ / / / _ \/ ___/ ___/ / __ \/ __ `/
 / /|  / /_/ / / / / / / /_/ /  __/ /     / /_/ / /_/ /  __(__  |__  ) / / / / /_/ / 
/_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/      \____/\__,_/\___/____/____/_/_/ /_/\__, /  
                                                                            /____/   
'''

print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking a number between 1 and 100.")

#select a number randomly
import random
number = random.randint(1,100)

#select mode
mode = input("Choose a difficulty. Type 'easy' or 'hard': ")

if mode == 'easy':
    number_guess = 10
else:
    number_guess = 5
print(f"You have {number_guess} remaining to guess the number")


guess = 0
while number_guess>0:
    guess = int(input("Make a guess: "))
    if guess!=number:
        if guess>number:
            print("Too high.")
        elif guess<number:
            print("Too low.")
        print("Guess again.")
        number_guess-=1
        print(f"You have {number_guess} remaining to guess the number")
    elif guess==number:
        print(f"You got it! The answer is {number}.")
        break
else:
    print("You've ran out of guesses, you lose.")




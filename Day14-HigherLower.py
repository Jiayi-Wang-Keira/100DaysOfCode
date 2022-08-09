from Day14Setup import logo,vs,data
import random

person_a = random.choice(data)
correct_answer = True
score = 0
print(logo)

while correct_answer == True:

    person_b = random.choice(data)
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
    print(vs)
    print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")
    guess = input("Who has more followers? Type A or B: ")

    follower_a = person_a['follower_count']
    follower_b = person_b['follower_count']

    if (follower_a>follower_b and guess=='A') or (follower_a<follower_b and guess=='B'):
        score += 1
        person_a = person_b
    else:
        correct_answer = False

    if correct_answer == False:
        print(f"Sorry, that\'s wrong. Final score: {score}.")
    else:
        print(f"You\'re correct, current score: {score}.")





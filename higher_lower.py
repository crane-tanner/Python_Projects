from art import logo, vs
from game_data import data
import random 
from replit import clear
print(logo)  

score = 0
is_true = True

def get_random_data():
    return random.choice(data)

def display_data(data_dict):
    name = data_dict['name']
    description = data_dict['description']
    country = data_dict['country']
    follower_count = data_dict['follower_count']
    print(f"{name}, a {description}, from {country},")
                                                  

A = get_random_data()
B = get_random_data()

while is_true:
    
    display_data(A)
    print(vs)
    display_data(B)

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if (guess == 'A' and A['follower_count'] > B['follower_count']) or (guess == 'B' and B['follower_count'] > A['follower_count']):
        clear()
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")
        is_true = False

    A = B  # Set A to the previous B
    B = get_random_data()  # Get new random data for B

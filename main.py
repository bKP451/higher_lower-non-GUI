from game_data import data
from game_art import logo, vs
import random
import os


def clear(): os.system('clear')


user_score = 0
game_finished = False
temp_dict = {}
first_option = random.choice(data)
temp_dict = first_option

while not game_finished:
    clear()
    print(logo)
    print(f"Compare A: {temp_dict['name']}, a {temp_dict['description']}, from {temp_dict['country']}  ")
    print(vs)
    second_option = random.choice(data)
    print(f"Against B: {second_option['name']}, a {second_option['description']}, from {second_option['country']}  ")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice == 'a':
        if temp_dict['follower_count'] > second_option['follower_count']:
            user_score = user_score + 1
            print(f"You are right. Current score {user_score}")
            temp_dict = second_option
        else:
            print(f"Sorry that's wrong. Final score : {user_score}")
            game_finished = True
    elif user_choice == 'b':
        if second_option['follower_count'] > temp_dict['follower_count']:
            user_score = user_score + 1
            print(f"You are right. Current score {user_score}")
            temp_dict = second_option
        else:
            print(f"Sorry that's wrong. Final score : {user_score}")
            game_finished = True




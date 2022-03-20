from game_data import data
from game_art import logo, vs
import random
import os

user_score = 0
def clear(): os.system('clear')


game_finished = False


def statements(entry):
    name = entry["name"]
    des = entry["description"]
    country = entry["country"]
    return f"{name}, a {des}, from {country}"


def compare(first_option, second_option, user_guess):
    # I can use boolean here
    if first_option['follower_count'] < second_option['follower_count']:
        return user_guess == 'b'
    else:
        return user_guess == 'a'


second_entry = random.choice(data)
while not game_finished:

    # Here I always have to compare the second_entry to the newly generated random entry
    first_entry = second_entry
    second_entry = random.choice(data)
    # first and  second entry should be unique
    if first_entry == second_entry:
        second_entry = random.choice(data)
    print(logo)
    print(f"Compare A: {statements(first_entry)}")
    print(vs)
    print(f"Against B: {statements(second_entry)}")

    guess = input("Who has more followers ? Type 'A' or 'B' ").lower()
    clear()
    if compare(first_entry, second_entry, guess):
        user_score = user_score + 1
        print(f"You guessed right !! Your score is {user_score}")
    else:
        print(f"Sorry you guessed it wrong. Score is {user_score}")
        game_finished = True



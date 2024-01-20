from art import logo, vs
from game_data import data
import random
import os

def format_data(account):    
    """Take the account data and returns printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and followr counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
print(logo)
score = 0
should_continue = True
account_b = random.choice(data)
while should_continue:
    account_a = account_b 
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")    
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for the guress
    guess = input("Who has more followers: Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_a["follower_count"]
    is_corrent = check_answer(guess, a_follower_count, b_follower_count)
    os.system('clear')
    print(logo)
    if is_corrent:
        score += 1
        print(f"You 're right! Currnet score: {score}")
    else:
        should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
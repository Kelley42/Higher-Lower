from art import logo, vs
from game_data import data
import random
import os

def play_game(first_thing, score):
    print(logo)
    article = article_choser(first_thing)
    first_thing["country"] = the_choser(first_thing)
    print(f"\nCompare A: {first_thing['name']}, {article} {first_thing['description'].lower()}, from {first_thing['country']}.")
    print(vs)
    # Get second piece of data, make sure it's not the same as first
    second_thing = random.choice(data)
    if second_thing == first_thing:
        second_thing = random.choice(data)
    article = article_choser(second_thing)
    second_thing["country"] = the_choser(second_thing)
    print(f"\nCompare B: {second_thing['name']}, {article} {second_thing['description'].lower()}, from {second_thing['country']}.")
    while True:
        choice = input("\nWho has more followers? Type 'A' or 'B': ").lower()
        if choice == 'a':
            if int(first_thing['follower_count']) > int(second_thing['follower_count']):
                print("\nCorrect!")
                score += 1
                play_game(first_thing, score)
            else:
                print(f"\nYou lose.\nYour score: {score}")
                play_again()
        elif choice == 'b':
            if int(first_thing['follower_count']) < int(second_thing['follower_count']):
                print("\nCorrect!")
                score += 1
                first_thing = second_thing
                play_game(first_thing, score)
            else:
                print(f"\nYou lose.\nYour score: {score}")
                play_again()
        else:
            print("\nIncorrect response - please try again.")

def article_choser(thing):
    """Depending on first letter of description, chooses the article before it"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    first_letter = thing['description'][0]
    if first_letter in vowels:
        new_article = "an"
    else:
        new_article = "a"
    return new_article

def the_choser(thing):
    """If country is United States or United Kingdom, add 'the' in front"""
    if thing["country"] == "United States":
        thing["country"] = "the United States"
    elif thing["country"] == "United Kingdom":
        thing["country"] = "the United Kingdom"
    else:
        thing["country"] = thing["country"]
    return thing["country"]

def play_again():
    """Takes input on play again and returns answer"""
    while True:
        play_again_input = input("\nDo you want to play again? 'y' or 'n': ").lower()
        if play_again_input == 'n':
            exit()
        elif play_again_input == 'y':
            os.system('clear')
            score = 0
            # Get first piece of data
            first_thing = random.choice(data)
            play_game(first_thing, score)
        else:
            print("Incorrect answer - please try again.")

score = 0
# Get first piece of data
first_thing = random.choice(data)
play_game(first_thing, score)
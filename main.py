#import the logo
from art import logo, vs
from game_data import data
import random 



#make a function to randomnly choose a data
def choice():
    return random.choice(data)

#make a function to print the description
def description(individual):
    name = individual["name"]
    description = individual["description"]
    country = individual["country"]
    print(f"{name}, a {description}, from {country}")

#compare the follower count of A and B (make a function)
def compare(a,b):
    followers_a =a["follower_count"]
    followers_b =b["follower_count"]
    if followers_a > followers_b:
        return "a" 
    else:
        return "b"

def game():
    print(logo)
    a = choice()
    description(a)
    print(vs)
    b = choice()
    description(b)
    greater_followers = compare(a,b)


    #Ask the user for input. that is who has the most number of followers
    user_input = input("Who has more followers? 'A' or 'B': ").lower()
    if user_input == greater_followers:
        print("You got it right")
    else:
        print("You are wrong")
#if the user guesses the number of followers right, then raise the score. show the score.

#if the user guesses the wrong answer, tell the user that they are wrong and print the score. then the game ends

game()



#import the logo
from art import logo, vs
from game_data import data
import random 



#make a function to randomnly choose a data
def choose():
    return random.choice(data)

#make an individual description function for both A and B.
def CompareA(a):
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")

def AgainstB(b):
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")


#compare the follower count of A and B (make a function)
def compare(a,b):
    followers_a = a["follower_count"]
    followers_b = b["follower_count"]
    if followers_a > followers_b:
        return "a" 
    else:
        return "b"

def game():
    print(logo)
    a = choose()
    
    #to keep track of the score. 
    score = 0
    #TODO put a flag here and make a while loop from here
    game_over = False
    while not game_over:
        CompareA(a)
        print(vs)
        b = choose()
        AgainstB(b)
        greater_followers = compare(a,b)
        
        #Ask the user for input. that is who has the most number of followers
        user_input = input("Who has more followers? 'A' or 'B': ").lower()
        if user_input == greater_followers:
            #if the user guesses the number of followers right, then raise the score. show the score.
            score += 1
            print(f"You got it right.")
            print(f"Score : {score}")
            a = b
        else:
            #if the user guesses the wrong answer, tell the user that they are wrong and print the score. then the game ends
            print(f"You are wrong. You lose. Your total score is {score}")
            game_over = True
        
    #ask the user if he wants to play again?
    choice = input("Do you want to play again?. Type 'y' for yes and 'n' for no. ").lower()
    if choice == "y":
        game()


game()



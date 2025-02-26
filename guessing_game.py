"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
import random
import statistics
from statistics import mode
from statistics import mean
from statistics import median

# Create the start_game function.

you_tried = []

def start_game():
# Write your code inside this function.
while True:
        bingo = 34 

        print("Welcome to the number guessing game!!!")
        your_name = input("Register your name: ")
        print(f"Hello {your_name}!!!")
    
        attempts = 0  

        while True:
            choosen_number = int(input("\n Guess a number from 0 to 100: "))  

            if choosen_number > 100 or choosen_number < 0:
                print("Oops, the number is outside of the range!! Please try again.")
                continue
        
            attempts += 1  

            if choosen_number > bingo:
                print("Too high, try lower.")
            elif choosen_number < bingo:
                print("Too low, try higher.")
            else: 
                print("Congrats, that's the number we've been looking for!")
            
                you_tried.append(attempts)
                        
                               
            
                break  
            
        print(f"\n \n You tried {attempts} times")
        tried= mode(you_tried)
        print(f"\n The most often seen attempt is: {tried}")
            
        mesi= mean(you_tried)
        print(f"\n The mean of your attempts is {mesi}")
            
        medi= median(you_tried)
        print (f"\nThe median of your attempts is {medi}")
    
    
        repeat=input("\n Do you wanna play again? yes/no:   ")
        if repeat !="yes":
            print("\n \n Thanks for playing")
            break
    
    
        

start_game()

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
#   5. Display the following data to the player
#     a. How many attempts it took them to get the correct number in this game
#     b. The mean of the saved attempts list
#     c. The median of the saved attempts list
#     d. The mode of the saved attempts list
#   6. Prompt the player to play again
#     a. If they decide to play again, start the game loop over.
#     b. If they decide to quit, show them a goodbye message.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.

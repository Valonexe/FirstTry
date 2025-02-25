import random
import statistics
from statistics import mode
from statistics import mean
from statistics import median

you_tried = []

def start_game():
    
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

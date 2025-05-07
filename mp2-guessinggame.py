import random
import os

def menu():
    print("---------------------------")
    print("   Number Guessing Game    ")
    print("---------------------------")
    print("[1] Play Game")
    print("[2] Exit")
    print("---------------------------")
 
#Clears terminal and waits for user before continuing   
def cls():
    input("\nPress Enter to return to Main Menu...")
    os.system('cls' if os.name =='nt' else 'clear')

def main():
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            number = random.randint(1, 100)     #Generates random number from 1-100
            counter = 1; guess = 0
            
            while guess != number:
                guess = int(input("Enter your guess(1-100): "))
                if guess < number:
                    print("Too low!")
                    counter += 1
                elif guess > number:
                    print("Too high!")
                    counter += 1
            else:
                print("You guessed it!")
                print(f"It took {counter} tries.")
                cls()
        elif choice == 2:
            print("Thank you for playing Number Guessing Game!")
            print("Program closing . . .")
            break
        else:
            print("Invalid input. Please try again.")
            cls()
                    
main()


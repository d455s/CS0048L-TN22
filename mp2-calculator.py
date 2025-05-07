import os

def menu():
    print("-------------------")
    print(" Python Calculator ")
    print("-------------------")
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[0] Exit")
    print("-------------------")


def add(x,y):
    return x+y 
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y == 0:
        return "Cannot divide by 0. Please try again."
    else:
        return x/y    

#Clears terminal and waits for user before continuing 
def cls():
    input("\nPress Enter to continue...")
    os.system('cls' if os.name =='nt' else 'clear')

def main():
    while True: 
        menu()
        choice = int(input("Enter your choice: "))
        if choice >= 1 and choice <= 4:
            x = int(input("Enter first number: "))
            y = int(input("Enter second number: "))

        if choice == 1:
            print("Result:", add(x,y))
            cls()
        elif choice == 2:
            print("Result:", sub(x,y))
            cls()
        elif choice == 3:
            print("Result:", mul(x,y))
            cls()
        elif choice == 4:
            print("Result:", div(x,y))
            cls()
        elif choice == 0:
            print("Thank you for using Python Calculator!")
            print("Program closing . . .")
            break
        else:
            print("Invalid input. Please try again.")
            cls()
            
main()
        
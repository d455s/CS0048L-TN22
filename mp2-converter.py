import os

def menu():
    print("---------------------------")
    print("   Temperature Converter   ")
    print("---------------------------")
    print("[1] Celsius to Fahrenheit")
    print("[2] Fahrenheit to Celsius")
    print("[0] Exit")
    print("---------------------------")

#Clears terminal and waits for user before continuing        
def cls():
    input("\nPress Enter to continue...")
    os.system('cls' if os.name =='nt' else 'clear')

c_to_f = lambda x : (x * 9/5) + 32
f_to_c = lambda x : (x - 32) * 5/9
    
def main():
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        if choice >= 1 and choice <= 2:
            x = int(input("Enter temperature: "))
            
        if choice == 1:
            print(f"Result: {c_to_f(x):.2f} ")      #Result is rounded to 2 decimal points
            cls()
        elif choice == 2:
            print(f"Result: {f_to_c(x):.2f}")       #Result is rounded to 2 decimal points
            cls()
        elif choice == 0:
            print("Thank you for using Temperature Converter!")
            print("Program closing . . .")
            break
        else:
            print("Invalid input. Please try again.")
            cls()
            
main()
import os

def menu():
    print("---------------------------")
    print("        To-Do List         ")
    print("---------------------------")
    print("[1] Add task")
    print("[2] Remove task")
    print("[3] View tasks")
    print("[0] Exit")
    print("---------------------------")

#Clears terminal and waits for user before continuing
def cls():
    input("\nPress Enter to continue...")
    os.system('cls' if os.name =='nt' else 'clear')
    
def main():
    tasks = []
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            addTask = input("Add a task: ")
            tasks.append(addTask)
            print("Task added succesfully!")
            cls()
        elif choice == 2:
            removeTask = input("Remove task: ")
            for task in tasks:
                if removeTask == task:
                    tasks.remove(removeTask)
                    print("Task removed successfully!")
                    cls()
                    break
            else:
                print("No match. Please try again.")
                cls()
        elif choice == 3:
            counter = 1
            if len(tasks) == 0:
                print("To-do list is empty. Please add a task first.")
            else:
                for task in tasks:
                    print(f"{counter}. {task}")
                    counter += 1
            cls()
        elif choice == 0:
            print("Thank you for using To-Do List!")
            print("Program closing . . .")
            break
        else:
            print("Invalid input. Please try again.")
            cls()

main()
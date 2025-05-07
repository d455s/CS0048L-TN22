import os

def menu():
    print("---------------------------")
    print(" Student Grade Calculator ")
    print("---------------------------")
    print("[1] Add Grade")
    print("[2] Calculate Average")
    print("[0] Exit")
    print("---------------------------")

#Clears terminal and waits for user before continuing    
def cls():
    input("\nPress Enter to continue...")
    os.system('cls' if os.name =='nt' else 'clear')
    
def main():
    grades = {}
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            subjName = input("Enter the subject name: ")
            subjGrade = int(input("Enter your grade: "))
            #Assigns/updates key value pairings in dict
            grades[subjName] = subjGrade
            print("Grade added successfully!")
            cls()
            
        elif choice == 2:
            avg = 0
            if len(grades) != 0:
                print("\nGrades Summary")
                #Displays each subject name and corresponding grade
                for name, grade in grades.items():
                    print(f"{name}: {grade}")
                    avg += grade
                print("---------------------------")
                avg /= len(grades)
                print(f"Average: {avg:.2f}") #Result is rounded to 2 decimal places
                cls()
            else:
                print("No grades found. Please try again.")
                cls()
            
        elif choice == 0:
            print("Thank you for using Student Grade Calculator!")
            print("Program closing . . .")
            break 
        
        else:
            print("Invalid input. Please try again.")
            cls()
            
main()
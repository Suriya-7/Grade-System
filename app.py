# This is Grade System project it will get inputs from users to generate the grade according to the given inputs
import app_logic

def main():
    print("Welcome to Grade System")
    print("----------------------------")
    print("1. Use Default Grade System")
    print("2. Use Custom Grade System")
    print("3. Exit")

    choice = input("Enter the choice from (1-3): ")

    if choice == '1':
        app_logic.default_grade_system()

    elif choice == '2':
        pass

    elif choice == '3':
        print("Exiting...")

    else:
        print("Invalide Choice.")

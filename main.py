# This is Grade System project it will get inputs from users to generate the grade according to the given inputs
import greeting


print("Welcome to Grade System")
print("----------------------------")
print("1. Use Default Grade System")
print("2. Use Custom Grade System")
print("3. Help")

choice = input("Enter the choice from (1-3): ")

if choice == 1:
    greeting.welcome_message()

elif choice == 2:
    pass

# default grade system process

def default_grade_system():

    #greeting message
    print("This is default grade system you can give upto 5 subject to calculate grade.")

    # let's get subject name from user's
    def subject_name():
        print("*****************************")
        subject1 = input("Enter First Subject Name: ")
        subject2 = input("Enter Second Subject Name: ")
        subject3 = input("Enter Third Subject Name: ")
        subject4 = input("Enter Fourth Subject Name: ")
        subject5 = input("Enter Fiveth Subject Name: ")
        print("*****************************")
        print("All Right!,")

    # Checking all the subject name or correct or not     
    print(f"Let's check all the subejct names \n 1.{subject_name.subject1}, \n 2.{subject_name.subject2}, \n 3.{subject_name.subject3}, \n 4.{subject_name.subject4},\n 5.{subject_name.subject5}")
    
    print("If all the subect name are correct Hit 1 or you want to change any subject name Hit 2")

    # validation of given subjects name 

    subject_validation = input("('1' or '2'): ")

    if subject_validation == '1':
        pass
    elif subject_validation == '2':
        subject_name()
    else: 
        print("Invalied Input.")
        
    def display_grade_system():

        # Displaying Default mark system to user's 

        print("This is a default grade system range.")
        print("B -> (50-60) \n B-plus -> (60-70) \n A -> (70-80) \n A-Plus -> (80-90) \n O-> (90-100)")
        print("Bellow '50' is consider as Fail. \n Let's enter marks for given subjects.")

        # Getting mark for given Subejct from User's 

        mark_for_sub1 = input(f"Enter mark for {subject_name.suject1}: ")
        mark_for_sub2 = input(f"Enter mark for {subject_name.suject2}: ")
        mark_for_sub3 = input(f"Enter mark for {subject_name.suject3}: ")
        mark_for_sub4 = input(f"Enter mark for {subject_name.suject4}: ")
        mark_for_sub5 = input(f"Enter mark for {subject_name.suject5}: ")
        print("All Right!")

    #Display all the marks and subject to user for verfication
    print("Let's Calculate the grade according to mark..")

    #Here calculating the mark along with grade system with if else statement 

    

    # this function will display all the subject name along with marks 
    def finalize():
        print("******************************************************")
        print(f"Subejct Name: {subject_name.subject1} Corresponding Mark: {display_grade_system.mark_for_sub1}")
        print(f"Subejct Name: {subject_name.subject2} Corresponding Mark: {display_grade_system.mark_for_sub2}")
        print(f"Subejct Name: {subject_name.subject3} Corresponding Mark: {display_grade_system.mark_for_sub3}")
        print(f"Subejct Name: {subject_name.subject4} Corresponding Mark: {display_grade_system.mark_for_sub4}")
        print(f"Subejct Name: {subject_name.subject5} Corresponding Mark: {display_grade_system.mark_for_sub5}")
        print("******************************************************")

    #That's all default grade system is done the work
print("I think, you get all the subjects, mark along with grade.")

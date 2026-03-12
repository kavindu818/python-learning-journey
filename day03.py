        # 1. If/Else Conditions

print("--- Web Technology Exam Checker ---")
exam_score = int(input("Enter your exam score:"))

if exam_score >= 50:
    print("Congratulations! You passed the Web Technology exam.")
    print("Now focus on your freelance skills.")

else:
    print("Don't give up! Review your short notes and try again.")


        # 2. For Loops

print("\n--- My Skill Checklist ---")

skills = ["Graphic Design","Video Editing","Python", "Git"]

choice = input("Do you want to check my skills: [Y/N]")
'''
                ක්‍රමය 1: එක පේළියෙන් වැඩේ ඉවර කිරීම (Best Practice)

                    choice = input("Do you want to check my skills? [Y/N]: ").lower()

                    if choice == "y":
                        print("Checking skills...")
                
                ------------------------------------------------------------

                ක්‍රමය 2: Check කරන වෙලාවට විතරක් Simple කිරීම

                    choice = input("Do you want to check my skills? [Y/N]: ")

                    if choice.lower() == "y":
                        print("Checking skills...")   
                                    
'''

if choice == "y" or choice == "Y":  #
    for skill in skills:
        print("I am practicing: " + skill)

elif choice == "n" or choice == "N":
    print("Thank you!")

else:
    print("Enter valid input")
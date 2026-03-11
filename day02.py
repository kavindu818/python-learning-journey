        # 1. Python Lists

tech_stack = ["Python","Git", "PHP","MySQL"]
print("My current tech stack:",tech_stack)

# add a item to the list

tech_stack.append("Vue.js")
print("Updated tech stack:", tech_stack)

        # 2. Python Functions

def greeting_developer(name,university):
    print("Welcome " + name + ", from " + university)
    print("Keep pushing towards that Software Engineering Internship.")

name = input("Enter your name:")
university = input("Enter your University:")

# Calling the function

greeting_developer(name,university)
 
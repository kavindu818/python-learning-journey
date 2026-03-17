# Day 7: Python Functions (Code Templates)
print("=== My Freelance ToolBox ===\n")

# 1. Defining a basic function (Creating a template)
# def means 'Define'.
def greet_client(client_name):
    print(f"Hello {client_name}, welcome to my portfolio!")
    print("I am a Software Engineering undergraduate at OUSL.\n")

# 2. Defining a function with calculations
def calculate_budget(hours):

    total = 0

    if hours <= 5 :
        if hours == 1:
            total=hours*10
        elif hours == 2:
            total=hours*15
        elif hours == 3:
            total=hours*20
        elif hours == 4:
            total=hours*25
        else:
            total=hours*30
    else:
        total= 150 + (hours-5)*10
        
    return total
    

# --- Using the functions ---

print("--- Sending automated replies ---")
client_name= input("Enter Your Name: ")

greet_client(client_name)

print("--- Calculating Project Costs ---")

hours= int(input("Enter the number of hours required: "))
my_price = calculate_budget(hours) 
print(f"Your total project cost will be: ${my_price}")
# Day 5: Mini-Project: Freelance Task Manager
print("=== My Freelance Task Manager ===")

# Store task using List and Dictionaries
tasks =[
    {"id":1, "title":"Edit weding video", "status":"Pending"},
    {"id":2, "title":"Design logo for cafe", "status":"Pending"}
]

# The While Loop that keeps the app running
while True:
    print("\nOptions:")
    print("1. View Task")
    print("2. Add a New Task")
    print("3. Mark Task as Done")
    print("4. Exit")

    choice= (int(input("\nEnter your choice (1-4):")))

    if choice == 1:
        print("\n--- Current Task ---")
        for task in tasks:
            # print using f-strings
            print(f"[{task['id']}] {task['title']} - {task['status']}")

    elif choice == 2:
        new_id = len(tasks) + 1             # create new id 
        new_title = input("Enter the new task title: ")
        # Add new details  
        new_task = {"id":new_id, "title": new_title, "status":"Pending"}
        tasks.append(new_task)
        print("Task Added succesfully!")

    elif choice == 3:
        task_id = int(input("Enter task ID to mark as done: "))
        found = False

        for task in tasks:
            if (task["id"]) == task_id:
                task["status"] = "Done" # Update the Status
                print("Task updated successfully!")
                found = True
                break
        if not found:
            print("Task not found! Please check the ID.")

    elif choice == 4 :
        print("Exiting Task Manager. Good luck with your freelance work!")
        break # break the loop

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

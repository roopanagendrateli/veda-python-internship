tasks = []


def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def update_task():
    view_tasks()

    if tasks:
        try:
            task_number = int(input("Enter task number to update: "))

            if 1 <= task_number <= len(tasks):
                new_task = input("Enter the new task: ")
                tasks[task_number - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")


def remove_task():
    view_tasks()

    if tasks:
        try:
            task_number = int(input("Enter task number to remove: "))

            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")


while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        print("Thank you for using the To-Do List!")
        break
    else:
        print("Invalid choice. Please try again.")
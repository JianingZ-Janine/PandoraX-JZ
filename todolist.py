import os

# File to store the tasks
TASKS_FILE = "BarbieTODO.txt"

def load_tasks():
    """Load tasks from the file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
        # Strip any extra newlines from the tasks
        tasks = [task.strip() for task in tasks]
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("What do you want to do, Barbie?: ")
    tasks.append(task)
    # Save the updated task list to the file
    save_tasks(tasks)
    print(f'Task "{task}" added!')

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("Barbie,you have no tasks in the list.")
    else:
        print("Your tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def remove_task(tasks):
    """Remove a task from the list."""
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            # Save the updated task list to the file
            save_tasks(tasks)
            print(f'Task "{removed_task}" removed!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number,barbie.")

def main():
    # Load tasks from the file at the start
    tasks = load_tasks()
    while True:
        # Display the menu
        print("\nBarbie To-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        # Take input from the user
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("You are the best! Goodbye Beautiful Barbie!")
            break
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()
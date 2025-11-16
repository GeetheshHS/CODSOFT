import json
import os

file_name = "todo_list.json"

def load_tasks():
    if os.path.exists(file_name):
        try:
            with open(file_name, 'r') as file:
                content = file.read().strip()
                if not content:
                    return []
                return json.loads(content)
        except json.JSONDecodeError:
            return []
    return []

def save_tasks(tasks):
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)

def view_tasks(tasks):
    if not tasks:
        print("No tasks found")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    title = input("Enter new task: ").strip()
    if title:
        tasks.append(title)
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task title cannot be empty.")

def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        num = int(input("Enter task number to update: "))
        if num < 1 or num > len(tasks):
            print("Invalid task number.")
            return

        new_title = input("Enter new title: ").strip()
        if new_title:
            tasks[num - 1] = new_title
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Title cannot be empty")

    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        num = int(input("Enter task number to delete: "))
        if num < 1 or num > len(tasks):
            print("Invalid task number.")
            return

        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed}")

    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTodo List")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Completed...")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()

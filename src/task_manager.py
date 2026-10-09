from data_manager import save_data
from validation import is_valid_text


def add_task(data, period):
    new_task = input("\nEnter task name: ").strip()
    new_subject = input("Enter subject: ").strip()

    if not is_valid_text(new_task):
        print("Task name cannot be empty.")
        return

    if not is_valid_text(new_subject):
        print("Subject cannot be empty.")
        return

    if new_subject not in period["subjects"]:
        print("Subject does not exist. Please add it first.")
        return

    task = {
        "name": new_task,
        "subject": new_subject,
        "completed": False
    }

    period["tasks"].append(task)
    save_data(data)

    print("Task added successfully!")


def view_tasks(period):
    tasks = period["tasks"]

    print("\nTasks:")

    if len(tasks) == 0:
        print("No tasks added yet.")
        return

    for task in tasks:
        status = "[✓]" if task["completed"] else "[ ]"
        print(status, task["name"], "|", task["subject"])

def complete_task(data, period):
    tasks = period["tasks"]

    if not tasks:
        print("\nNo tasks available to complete.")
        return

    print("\nTasks:")

    for index, task in enumerate(tasks, start=1):
        status = "[✓]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['name']} | {task['subject']}")

    choice = input("\nEnter the task number to complete: ").strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return

    task = tasks[index]

    if task["completed"]:
        print("This task is already completed!")
        return

    task["completed"] = True
    save_data(data)

    print("Task marked as completed! 🎉")
from data_manager import save_data
from validation import is_valid_text
from datetime import datetime


# -----------------------------------------
# ADD TASK
# -----------------------------------------

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

    due_date = input(
        "Enter due date (YYYY-MM-DD), or leave blank: "
    ).strip()

    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD, such as 2026-10-15.")
            return

    task = {
        "name": new_task,
        "subject": new_subject,
        "completed": False,
        "due_date": due_date if due_date else None
    }

    period["tasks"].append(task)
    save_data(data)

    print("Task added successfully! 🎉")


# -----------------------------------------
# VIEW TASKS
# -----------------------------------------

def view_tasks(period):
    tasks = period["tasks"]

    print("\nTasks:")

    if not tasks:
        print("No tasks added yet.")
        return

    for task in tasks:
        status = "[✓]" if task["completed"] else "[ ]"
        due_date = task.get("due_date") or "No deadline"

        print(
            f"{status} {task['name']} | "
            f"{task['subject']} | "
            f"Due: {due_date}"
        )


# -----------------------------------------
# COMPLETE TASK
# -----------------------------------------

def complete_task(data, period):
    tasks = period["tasks"]

    if not tasks:
        print("\nNo tasks available to complete.")
        return

    print("\nTasks:")

    for index, task in enumerate(tasks, start=1):
        status = "[✓]" if task["completed"] else "[ ]"
        due_date = task.get("due_date") or "No deadline"

        print(
            f"{index}. {status} {task['name']} | "
            f"{task['subject']} | Due: {due_date}"
        )

    choice = input(
        "\nEnter the task number to complete: "
    ).strip()

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


# -----------------------------------------
# EDIT TASK
# -----------------------------------------

def edit_task(data, period):
    tasks = period["tasks"]

    if not tasks:
        print("\nNo tasks available to edit.")
        return

    print("\nTasks:")

    for index, task in enumerate(tasks, start=1):
        status = "[✓]" if task["completed"] else "[ ]"
        due_date = task.get("due_date") or "No deadline"

        print(
            f"{index}. {status} {task['name']} | "
            f"{task['subject']} | Due: {due_date}"
        )

    choice = input(
        "\nEnter the task number to edit: "
    ).strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return

    task = tasks[index]

    print("\nLeave a field blank to keep its current value.")
    print("Enter 0 as the due date to remove the deadline.")

    new_name = input(
        f"Task name [{task['name']}]: "
    ).strip()

    new_subject = input(
        f"Subject [{task['subject']}]: "
    ).strip()

    current_due_date = task.get("due_date") or "No deadline"

    new_due_date = input(
        f"Due date [{current_due_date}]: "
    ).strip()

    candidate_name = (
        new_name if new_name else task["name"]
    )

    candidate_subject = (
        new_subject if new_subject else task["subject"]
    )

    candidate_due_date = task.get("due_date")

    # Validate the proposed deadline first.
    if new_due_date == "0":
        candidate_due_date = None

    elif new_due_date:
        try:
            datetime.strptime(new_due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD. Changes cancelled.")
            return

        candidate_due_date = new_due_date

    # Validate all proposed values before changing the task.
    if not is_valid_text(candidate_name):
        print("Task name cannot be empty.")
        return

    if candidate_subject not in period["subjects"]:
        print("Subject does not exist in this period. Changes cancelled.")
        return

    # Apply changes only after validation succeeds.
    task["name"] = candidate_name
    task["subject"] = candidate_subject
    task["due_date"] = candidate_due_date

    save_data(data)

    print("Task updated successfully! 🎉")


# -----------------------------------------
# DELETE TASK
# -----------------------------------------

def delete_task(data, period):
    tasks = period["tasks"]

    if not tasks:
        print("\nNo tasks available to delete.")
        return

    print("\nTasks:")

    for index, task in enumerate(tasks, start=1):
        status = "[✓]" if task["completed"] else "[ ]"
        due_date = task.get("due_date") or "No deadline"

        print(
            f"{index}. {status} {task['name']} | "
            f"{task['subject']} | Due: {due_date}"
        )

    choice = input(
        "\nEnter the task number to delete: "
    ).strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return

    task = tasks[index]

    print(f"\nTask selected: {task['name']}")

    confirmation = input(
        "Are you sure you want to delete this task? (y/n): "
    ).strip().lower()

    if confirmation != "y":
        print("Deletion cancelled.")
        return

    tasks.pop(index)
    save_data(data)

    print("Task deleted successfully! 🗑️")

# -----------------------------------------
# SEARCH TASKS
# -----------------------------------------

def search_tasks(period):
    tasks = period["tasks"]

    if not tasks:
        print("\nNo tasks available to search.")
        return

    keyword = input("\nEnter a task name or keyword: ").strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    matching_tasks = []

    for task in tasks:
        if keyword in task["name"].lower():
            matching_tasks.append(task)

    print("\nSearch Results:")

    if not matching_tasks:
        print("No matching tasks found.")
        return

    for task in matching_tasks:
        status = "[✓]" if task["completed"] else "[ ]"
        due_date = task.get("due_date") or "No deadline"

        print(
            f"{status} {task['name']} | "
            f"{task['subject']} | "
            f"Due: {due_date}"
        )

    print(f"\nFound {len(matching_tasks)} matching task(s).")
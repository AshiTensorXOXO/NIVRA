from data_manager import save_data
from validation import is_valid_text

def add_task(subjects, tasks):
    new_task = input("\nEnter task name: ").strip()
    new_subject = input("Enter subject: ").strip()

    if not is_valid_text(new_task):
        print("Task name cannot be empty.")
        return

    if not is_valid_text(new_subject):
        print("Subject cannot be empty.")
        return

    task = {
        "name": new_task,
        "subject": new_subject,
        "completed": False
    }

    tasks.append(task)

    save_data(subjects, tasks)

    print("Task added successfully!")

def view_tasks(tasks):
    print("\nTasks:")

    if len(tasks) == 0:
        print("No tasks added yet.")

    else:
        for task in tasks:
            if task["completed"]:
                status = "[✓]"
            else:
                status = "[ ]"

            print(status, task["name"], "|", task["subject"])
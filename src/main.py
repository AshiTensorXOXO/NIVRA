from data_manager import load_data, save_data
from validation import is_valid_text

print("==============================")
print("            NIVRA")
print("      Student Companion")
print("==============================")



data = load_data()

subjects = data["subjects"]
tasks = data["tasks"]



def view_subjects():
    print("\nSubjects:")

    for subject in subjects:
        print("-", subject)





def add_subject():
    new_subject = input("\nEnter subject name: ").strip()

    if not is_valid_text(new_subject):
        print("Subject name cannot be empty.")
        return

    subjects.append(new_subject)

    save_data(subjects, tasks)

    print("Subject added successfully!")




def view_tasks():
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





def add_task():
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



while True:

    print()
    print("===============================")
    print("1. View Subjects")
    print("2. Add Subject")
    print("3. View Tasks")
    print("4. Add Task")
    print("5. Complete Task")
    print("6. Exit")
    print("===============================")

    choice = input("\n >>> Enter your choice: ")

    if choice == "1":
        view_subjects()

    elif choice == "2":
        add_subject()

    elif choice == "3":
        view_tasks()

    elif choice == "4":
        add_task()

    elif choice == "5":
        complete_task()

    elif choice == "6":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice.")
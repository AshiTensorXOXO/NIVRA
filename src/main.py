from data_manager import load_data, save_data
from validation import is_valid_text
from task_manager import view_tasks, add_task

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
        view_tasks(tasks)

    elif choice == "4":
        add_task(subjects, tasks)

    elif choice == "5":
        complete_task()

    elif choice == "6":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice.")
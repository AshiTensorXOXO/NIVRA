from data_manager import load_data, save_data

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
    tasks.append(task)

    save_data(subjects, tasks)

    print("Task added successfully!")


def complete_task():
    tasks[task_number - 1]["completed"] = True

    save_data(subjects, tasks)

    print("Task completed!")



while True:

    print()
    print("1. View Subjects")
    print("2. Add Subject")
    print("3. View Tasks")
    print("4. Add Task")
    print("5. Complete Task")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

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
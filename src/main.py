print("==============================")
print("            NIVRA")
print("      Student Companion")
print("==============================")

subjects = [
    "Python",
    "C Programming",
    "C++",
    "Artificial Intelligence",
    "Machine Learning"
]

tasks = [
    {
        "name": "Complete Python assignment",
        "subject": "Python"
    },
    {
        "name": "Revise if-else",
        "subject": "C Programming"
    }
]

while True:

    print()
    print("1. View Subjects")
    print("2. Add Subject")
    print("3. View Tasks")
    print("4. Add Task")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\nSubjects:")

        for subject in subjects:
            print("-", subject)

    elif choice == "2":
        new_subject = input("\nEnter subject name: ")
        subjects.append(new_subject)
        print("Subject added successfully!")

    elif choice == "3":
        print("\nTasks:")

        if len(tasks) == 0:
            print("No tasks added yet.")

        else:
            for task in tasks:
                print("-", task["name"], "|", task["subject"])

    elif choice == "4":
        new_task = input("\nEnter task name: ")
        new_subject = input("Enter subject: ")

        task = {
            "name": new_task,
            "subject": new_subject
        }

        tasks.append(task)

        print("Task added successfully!")

    elif choice == "5":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice.")
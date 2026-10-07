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
        "subject": "Python",
        "completed": False
    },
    {
        "name": "Revise if-else",
        "subject": "C Programming",
        "completed": False
    }
]

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
                if task["completed"]:
                    status = "[✓]"
                else:
                    status = "[ ]"

                print(status, task["name"], "|", task["subject"])

    elif choice == "4":
        new_task = input("\nEnter task name: ")
        new_subject = input("Enter subject: ")

        task = {
            "name": new_task,
            "subject": new_subject,
            "completed": False
        }

        tasks.append(task)

        print("Task added successfully!")

    elif choice == "5":
        print("\nTasks:")

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i]["name"], "|", tasks[i]["subject"])

            task_number = int(input("\nEnter task number to complete: "))

            if task_number >= 1 and task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print("Task completed!")

            else:
                print("Invalid task number.")

    else:
        print("\nInvalid choice.")
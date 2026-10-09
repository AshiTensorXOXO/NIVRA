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
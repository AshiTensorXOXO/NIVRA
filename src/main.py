from data_manager import load_data, save_data
from task_manager import add_task, view_tasks, complete_task
from validation import is_valid_text


data = load_data()


def choose_academic_system():
    print("\nChoose your academic system:")
    print("1. Terms")
    print("2. Semesters")
    print("3. Quarters")
    print("4. Trimesters")
    print("5. Custom")

    choices = {
        "1": "Terms",
        "2": "Semesters",
        "3": "Quarters",
        "4": "Trimesters",
        "5": "Custom"
    }

    choice = input("Enter your choice: ").strip()

    if choice not in choices:
        print("Invalid choice.")
        return

    data["academic_system"] = choices[choice]
    save_data(data)
    print("Academic system saved!")


def add_period():
    if data["academic_system"] is None:
        print("\nChoose your academic system first.")
        return

    period_name = input(
        f"\nEnter {data['academic_system'][:-1].lower()} name: "
    ).strip()

    if not is_valid_text(period_name):
        print("Period name cannot be empty.")
        return

    for period in data["periods"]:
        if period["name"] == period_name:
            print("That period already exists.")
            return

    data["periods"].append({
        "name": period_name,
        "subjects": [],
        "tasks": []
    })

    save_data(data)
    print("Academic period added successfully!")


def view_periods():
    print("\nAcademic periods:")

    if not data["periods"]:
        print("No academic periods added yet.")
        return

    for index, period in enumerate(data["periods"], start=1):
        print(f"{index}. {period['name']}")


def select_period():
    if not data["periods"]:
        print("\nNo academic periods available.")
        return None

    view_periods()

    choice = input("\nEnter the period number: ").strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        return None

    index = int(choice) - 1

    if index < 0 or index >= len(data["periods"]):
        print("Invalid period number.")
        return None

    return data["periods"][index]


def add_subject(period):
    subject = input("\nEnter subject name: ").strip()

    if not is_valid_text(subject):
        print("Subject name cannot be empty.")
        return

    if subject in period["subjects"]:
        print("Subject already exists in this period.")
        return

    period["subjects"].append(subject)
    save_data(data)
    print("Subject added successfully!")

def rename_subject(period):
    if not period["subjects"]:
        print("\nNo subjects available to rename.")
        return

    view_subjects(period)

    old_name = input("\nEnter the subject to rename: ").strip()

    if old_name not in period["subjects"]:
        print("Subject does not exist.")
        return

    new_name = input("Enter the new subject name: ").strip()

    if not is_valid_text(new_name):
        print("Subject name cannot be empty.")
        return

    if new_name in period["subjects"]:
        print("A subject with that name already exists.")
        return

    index = period["subjects"].index(old_name)
    period["subjects"][index] = new_name

    for task in period["tasks"]:
        if task["subject"] == old_name:
            task["subject"] = new_name

    save_data(data)
    print("Subject renamed successfully!")


def view_subjects(period):
    print(f"\nSubjects in {period['name']}:")

    if not period["subjects"]:
        print("No subjects added yet.")
        return

    for index, subject in enumerate(period["subjects"], start=1):
        print(f"{index}. {subject}")


def remove_subject(period):
    if not period["subjects"]:
        print("\nNo subjects available to remove.")
        return

    view_subjects(period)

    subject = input("\nEnter the subject to remove: ").strip()

    if subject not in period["subjects"]:
        print("Subject does not exist.")
        return

    for task in period["tasks"]:
        if task["subject"] == subject:
            print("Cannot remove a subject linked to existing tasks.")
            return

    period["subjects"].remove(subject)
    save_data(data)
    print("Subject removed successfully!")


def period_menu(period):
    while True:
        print(f"\n===== {period['name']} =====")
        print("1. View subjects")
        print("2. Add subject")
        print("3. Rename subject")
        print("4. Remove subject")
        print("5. View tasks")
        print("6. Add task")
        print("7. Complete task")
        print("8. Back to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_subjects(period)

        elif choice == "2":
            add_subject(period)

        elif choice == "3":
            rename_subject(period)

        elif choice == "4":
            remove_subject(period)

        elif choice == "5":
            view_tasks(period)

        elif choice == "6":
            add_task(data, period)

        elif choice == "7":
            complete_task(data, period)

        elif choice == "8":
            break

        else:
            print("Invalid choice. Try again.")


def main():
    while True:
        print("\n========== NIVRA ==========")
        print("1. Choose academic system")
        print("2. Add academic period")
        print("3. View academic periods")
        print("4. Open an academic period")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            choose_academic_system()

        elif choice == "2":
            add_period()

        elif choice == "3":
            view_periods()

        elif choice == "4":
            period = select_period()

            if period is not None:
                period_menu(period)

        elif choice == "5":
            print("\nNivra says goodbye. Keep building!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
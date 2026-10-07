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
        print("\nTasks")

    elif choice == "4":
        print("\nAdd Task")

    elif choice == "5":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice.")
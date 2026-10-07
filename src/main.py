print("==============================")
print("            NIVRA")
print("      Student Companion")
print("==============================")

print()
print("1. View Subjects")
print("2. View Tasks")
print("3. Add Task")
print("4. Exit")

subjects = [
    "Python",
    "C Programming",
    "C++",
    "Artificial Intelligence",
    "Machine Learning"
]

choice = input("\nEnter your choice: ")

if choice == "1":
    print("\nSubjects:")
    
    for subject in subjects:
        print("-", subject)

elif choice == "2":
    print("\nTasks")

elif choice == "3":
    print("\nAdd Task")

elif choice == "4":
    print("\nGoodbye!")

else:
    print("\nInvalid choice.")
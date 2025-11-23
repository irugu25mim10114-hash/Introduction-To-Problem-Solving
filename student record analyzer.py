# ---------------------------------------------
# Student Record Analyzer - Console Application
# ---------------------------------------------

students = []

# Function 1: Add Student
def add_student():
    print("\n--- Add New Student ---")
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks (0-100): "))

    grade = calculate_grade(marks)

    student = {
        "roll": roll,
        "name": name,
        "marks": marks,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")

# Function 2: Grade Calculation
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

# Function 3: Display All Students
def display_students():
    print("\n--- Student Records ---")
    if not students:
        print("No records found.\n")
        return

    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}, Grade: {s['grade']}")
    print()

# Function 4: Search Student
def search_student():
    print("\n--- Search Student By Roll Number ---")
    roll = input("Enter Roll Number: ")

    found = False
    for s in students:
        if s['roll'] == roll:
            print("Record Found!")
            print(f"Name: {s['name']}, Marks: {s['marks']}, Grade: {s['grade']}\n")
            found = True
            break

    if not found:
        print("No student found with that roll number.\n")

# Function 5: Sort Students
def sort_students():
    print("\n--- Sort Students By Marks (High to Low) ---")
    if not students:
        print("No records to sort.\n")
        return

    sorted_list = sorted(students, key=lambda x: x['marks'], reverse=True)

    for s in sorted_list:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}, Grade: {s['grade']}")
    print()

# Function 6: Delete Student
def delete_student():
    print("\n--- Delete Student Record ---")
    roll = input("Enter Roll Number: ")

    global students
    students = [s for s in students if s['roll'] != roll]

    print("If record existed, it has been deleted.\n")

# Function 7: Menu
def menu():
    while True:
        print("""
====== Student Record Analyzer ======
1. Add Student
2. Display All Students
3. Search Student
4. Sort Students by Marks
5. Delete Student
6. Exit
""")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            sort_students()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run Application
menu()

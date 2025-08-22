# -------------------------------
# Student Grade & Attendance System
# -------------------------------

# Global dictionary to store student data
students = {}

# Function to add a new student
def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    # dictionary for each student
    student_data = {
        "grades": [],        # list for storing marks
        "attendance": 0      # attendance count
    }
    students[roll_no] = (name, student_data)  # tuple + dictionary

    print(f"✅ Student {name} (Roll No: {roll_no}) added successfully!\n")

# Function to add marks
def add_marks():
    roll_no = input("Enter roll number: ")

    if roll_no in students:
        marks = int(input("Enter marks: "))
        students[roll_no][1]["grades"].append(marks)   # list inside dict
        print(f"✅ Marks added for {students[roll_no][0]}\n")
    else:
        print("❌ Student not found!\n")

# Function to mark attendance
def mark_attendance():
    roll_no = input("Enter roll number: ")

    if roll_no in students:
        students[roll_no][1]["attendance"] += 1
        print(f"✅ Attendance marked for {students[roll_no][0]}\n")
    else:
        print("❌ Student not found!\n")

# Function to calculate average grade
def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

# Function to display student report
def student_report():
    roll_no = input("Enter roll number: ")

    if roll_no in students:
        name, data = students[roll_no]  # tuple unpacking
        avg_grade = calculate_average(data["grades"])  # function call

        print("\n----- Student Report -----")
        print(f"Name: {name}")
        print(f"Roll No: {roll_no}")
        print(f"Grades: {data['grades']}")
        print(f"Average Grade: {avg_grade}")
        print(f"Attendance: {data['attendance']} days")
        print("---------------------------\n")
    else:
        print("❌ Student not found!\n")

# Function to show all students
def show_all_students():
    if not students:
        print("No students available!\n")
        return
    
    print("\n===== All Students =====")
    for roll_no, (name, data) in students.items():
        print(f"Roll No: {roll_no} | Name: {name} | Attendance: {data['attendance']} | Grades: {data['grades']}")
    print("========================\n")

# Main menu loop
def main():
    while True:
        print("📘 Student Grade & Attendance System")
        print("1. Add Student")
        print("2. Add Marks")
        print("3. Mark Attendance")
        print("4. Student Report")
        print("5. Show All Students")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_marks()
        elif choice == "3":
            mark_attendance()
        elif choice == "4":
            student_report()
        elif choice == "5":
            show_all_students()
        elif choice == "6":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

# Run program
if _name_ == "_main_":
    main()
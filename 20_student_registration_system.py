"""
Q20. Final Challenge - Student Registration System
Build a menu-driven application using functions + for loops + while loops.
The system should allow users to add a student, view all students, search by
ID, update student details, delete a student, calculate class average marks,
display the highest-performing student, and exit. Store the records using
appropriate Python data structures.
"""

students = {}


def add_student():
    student_id = input("Enter student ID: ")
    if student_id in students:
        print("Student ID already exists")
        return
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    students[student_id] = {"name": name, "marks": marks}
    print("Student added successfully")


def view_students():
    if len(students) == 0:
        print("No students found")
    else:
        for student_id in students:
            print("ID:", student_id, "| Name:", students[student_id]["name"],
                  "| Marks:", students[student_id]["marks"])


def search_student():
    student_id = input("Enter student ID to search: ")
    if student_id in students:
        print("Name:", students[student_id]["name"])
        print("Marks:", students[student_id]["marks"])
    else:
        print("Student not found")


def update_student():
    student_id = input("Enter student ID to update: ")
    if student_id in students:
        name = input("Enter new name: ")
        marks = float(input("Enter new marks: "))
        students[student_id] = {"name": name, "marks": marks}
        print("Student updated successfully")
    else:
        print("Student not found")


def delete_student():
    student_id = input("Enter student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully")
    else:
        print("Student not found")


def class_average():
    if len(students) == 0:
        print("No students found")
        return
    total = 0
    for student_id in students:
        total = total + students[student_id]["marks"]
    average = total / len(students)
    print("Class average marks:", average)


def top_student():
    if len(students) == 0:
        print("No students found")
        return
    top_id = None
    highest = -1
    for student_id in students:
        if students[student_id]["marks"] > highest:
            highest = students[student_id]["marks"]
            top_id = student_id
    print("Top student:", students[top_id]["name"], "with", highest, "marks")


while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Class Average")
    print("7. Highest-Performing Student")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        class_average()
    elif choice == "7":
        top_student()
    elif choice == "8":
        print("Goodbye")
        break
    else:
        print("Invalid choice")

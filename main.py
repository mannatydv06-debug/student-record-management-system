
import json
import os

FILE_NAME = "students.json"


def load_records():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Error reading saved records.")

    return {}


def save_records():
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)
    except OSError:
        print("Error saving student records.")


students = load_records()


def add_student():
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Enter student name: ").strip()
    age = input("Enter student age: ").strip()
    course = input("Enter course: ").strip()
    marks = input("Enter marks (0-100): ").strip()

    if not name or not course:
        print("Name and course cannot be empty.")
        return

    try:
        age = int(age)
        marks = float(marks)

        if age <= 0 or not 0 <= marks <= 100:
            print("Invalid age or marks.")
            return

    except ValueError:
        print("Age must be an integer and marks must be numeric.")
        return

    students[student_id] = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    save_records()
    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- All Student Records ---")

    for student_id, details in students.items():
        print(f"\nStudent ID: {student_id}")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Course: {details['course']}")
        print(f"Marks: {details['marks']}")


def search_student():
    student_id = input("Enter student ID to search: ").strip()

    if student_id in students:
        details = students[student_id]

        print("\n--- Student Details ---")
        print(f"Student ID: {student_id}")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Course: {details['course']}")
        print(f"Marks: {details['marks']}")
    else:
        print("Student not found.")


def update_student():
    student_id = input("Enter student ID to update: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    details = students[student_id]

    print("Press Enter to keep the existing value.")

    name = input(f"Name [{details['name']}]: ").strip()
    age = input(f"Age [{details['age']}]: ").strip()
    course = input(f"Course [{details['course']}]: ").strip()
    marks = input(f"Marks [{details['marks']}]: ").strip()

    try:
        new_age = int(age) if age else details["age"]
        new_marks = float(marks) if marks else details["marks"]

        if new_age <= 0 or not 0 <= new_marks <= 100:
            print("Invalid age or marks.")
            return

    except ValueError:
        print("Enter valid numeric values.")
        return

    if name:
        details["name"] = name

    if age:
        details["age"] = new_age

    if course:
        details["course"] = course

    if marks:
        details["marks"] = new_marks

    save_records()
    print("Student record updated successfully!")


def delete_student():
    student_id = input("Enter student ID to delete: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    confirm = input(
        "Are you sure you want to delete this record? (yes/no): "
    ).strip().lower()

    if confirm == "yes":
        del students[student_id]
        save_records()
        print("Student record deleted successfully!")
    else:
        print("Deletion cancelled.")


def main():
    while True:
        print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

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
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

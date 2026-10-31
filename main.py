
import csv

PASS_MARK = 40
MIN_ATTENDANCE = 75
SUBJECTS = ["Python", "DBMS", "Mathematics", "Computer Networks", "English"]

students = []


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= PASS_MARK:
        return "E"
    return "F"


def get_integer(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(prompt))
            if minimum <= value <= maximum:
                return value
            print(f"Enter a number from {minimum} to {maximum}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def add_student():
    print("\n--- Add Student ---")

    roll_no = input("Enter roll number: ").strip()
    if not roll_no:
        print("Roll number cannot be empty.")
        return

    if any(s["roll_no"].lower() == roll_no.lower()
           for s in students):
        print("This roll number already exists.")
        return

    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    marks = {}
    for subject in SUBJECTS:
        marks[subject] = get_integer(
            f"Enter marks in {subject} (0-100): ", 0, 100
        )

    attendance = get_integer("Enter attendance percentage (0-100): ", 0, 100)

    total = sum(marks.values())
    percentage = total / len(SUBJECTS)
    failed_subjects = [
        subject for subject, score in marks.items()
        if score < PASS_MARK
    ]

    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": calculate_grade(percentage),
        "attendance": attendance,
        "result": "Fail" if failed_subjects else "Pass",
        "failed_subjects": failed_subjects,
    }

    students.append(student)
    print(f"\nStudent {name} added successfully!")
    display_student(student)


def display_student(student):
    print(f"\nRoll Number: {student['roll_no']}")
    print(f"Name: {student['name']}")

    for subject, score in student["marks"].items():
        print(f"{subject}: {score}/100")

    print(f"Total: {student['total']}/{len(SUBJECTS) * 100}")
    print(f"Percentage: {student['percentage']:.2f}%")
    print(f"Grade: {student['grade']}")
    print(f"Result: {student['result']}")
    print(f"Attendance: {student['attendance']}%")

    if student["attendance"] < MIN_ATTENDANCE:
        print("Attendance Warning: Below 75%")

    if student["failed_subjects"]:
        print("Subjects below pass mark:",
              ", ".join(student["failed_subjects"]))


def view_all_students():
    print("\n--- All Students ---")

    if not students:
        print("No student records available.")
        return

    for student in students:
        display_student(student)
        print("-" * 35)


def search_student():
    roll_no = input("Enter roll number to search: ").strip()

    for student in students:
        if student["roll_no"].lower() == roll_no.lower():
            display_student(student)
            return

    print("Student not found.")


def show_class_report():
    if not students:
        print("Add students before viewing class statistics.")
        return

    average = sum(s["percentage"] for s in students) / len(students)
    topper = max(students, key=lambda s: s["percentage"])
    passed = sum(s["result"] == "Pass" for s in students)
    attendance_warnings = sum(
        s["attendance"] < MIN_ATTENDANCE for s in students
    )

    print("\n--- Class Performance Report ---")
    print(f"Total students: {len(students)}")
    print(f"Class average: {average:.2f}%")
    print(f"Students passing all subjects: {passed}")
    print(f"Students failing at least one subject: {len(students) - passed}")
    print(f"Students below 75% attendance: {attendance_warnings}")
    print(f"Topper: {topper['name']} ({topper['percentage']:.2f}%)")


def export_csv():
    if not students:
        print("No records to export.")
        return

    filename = "student_report.csv"
    headers = [
        "Roll Number", "Name", *SUBJECTS, "Total",
        "Percentage", "Grade", "Result", "Attendance"
    ]

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()

            for student in students:
                row = {
                    "Roll Number": student["roll_no"],
                    "Name": student["name"],
                    **student["marks"],
                    "Total": student["total"],
                    "Percentage": f"{student['percentage']:.2f}",
                    "Grade": student["grade"],
                    "Result": student["result"],
                    "Attendance": student["attendance"],
                }
                writer.writerow(row)

        print(f"Report exported to {filename}")
    except OSError as error:
        print(f"Could not export report: {error}")


def main():
    while True:
        print("\n==============================")
        print(" STUDENT PERFORMANCE ANALYZER")
        print("==============================")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Class performance report")
        print("5. Export report to CSV")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            show_class_report()
        elif choice == "5":
            export_csv()
        elif choice == "6":
            print("Thank you for using Student Performance Analyzer!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()

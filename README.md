
# Student Performance Analyzer

A beginner-friendly Python college project that analyzes student
marks, calculates grades, monitors attendance, and generates
class performance reports.

## Features

- Register students using unique roll numbers
- Store marks for five subjects
- Calculate total marks and percentage
- Assign grades from A+ to F
- Identify students failing any subject
- Flag students with attendance below 75%
- Search for students by roll number
- Calculate class average and identify the topper
- Export student reports to CSV

## Technologies Used

- Python 3
- CSV module
- Python standard library

## Subjects

1. Python
2. DBMS
3. Mathematics
4. Computer Networks
5. English

Each subject is marked out of 100.

## Grading System

| Percentage | Grade |
|---|---|
| 90-100 | A+ |
| 80-89.99 | A |
| 70-79.99 | B |
| 60-69.99 | C |
| 50-59.99 | D |
| 40-49.99 | E |
| Below 40 | F |

A student passes only if every subject score is at least 40.

Attendance below 75% triggers a warning.

## How to Run

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   python main.py

5. Choose an option from the menu.

## Exporting Reports

Choose option 5 to create `student_report.csv`.
Open the CSV file using Excel, Google Sheets, or another
spreadsheet application.

The report contains student marks, total, percentage,
grade, result, and attendance.

## Project Structure

    student-performance-analyzer/
    ├── main.py
    ├── README.md
    ├── requirements.txt
    └── .gitignore

## Limitations

- Student records remain in memory while the program runs.
- Records are not automatically saved between sessions.
- The CSV export saves a report, not a database for reloading.

## Future Improvements

- Store records in SQLite
- Add a graphical user interface
- Generate performance charts
- Import student data from CSV
- Add a teacher login system

## Academic Use

This project is intended for learning Python programming,
conditional statements, loops, functions, dictionaries,
lists, input validation, and CSV file handling.

Developed as a Python mini-project for academic learning.

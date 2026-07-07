# Collection-Maniputator

# Student Data Organizer

A simple **Python console application** for managing student records using a menu-driven interface.  
This project uses Python `match-case` to handle user choices cleanly and efficiently.

# Objective

Student Data Organizer is a console-based Python application designed to efficiently manage student records through a user-friendly, menu-driven interface. The project demonstrates the implementation of core Python programming concepts, including functions, loops, conditional statements, string manipulation, collections (lists, tuples, sets, and dictionaries), data mutability, type casting, and the del keyword. It provides hands-on experience with CRUD (Create, Read, Update, Delete) operations while promoting clean code organization, modular programming, and problem-solving skills.

## Features

- Add new student records.
- Display all saved student details.
- Update existing student information.
- Delete student records.
- Display subjects for a specific student.
- Easy menu-based navigation using `match-case`.

## Technologies Used

- Python 3.10+
- Console / Terminal Input Output
- `match-case` statement

## How It Works

The program stores student information in a dictionary and lets the user perform different actions from a menu.  
Each menu option is handled using Python `match-case`, which makes the code cleaner and easier to read.

## Menu Options

1. Add Student
2. Display All Students
3. Update Student
4. Delete Student
5. Display Subjects
6. Exit

## Sample Console Output

```text
Welcome To The Student Data Organizer!

===== Student Data Organizer =====
1. Add Student
2. Display All Students
3. Update Student
4. Delete Student
5. Display Subjects
6. Exit
Enter your choice:
```

## Code Overview

### Add Student
Stores student details such as:
- Student ID
- Name
- Age
- Grade
- Date of Birth
- Subjects

### Display All Students
Shows all student records stored in the dictionary.

### Update Student
Updates an existing student's information by Student ID.

### Delete Student
Removes a student record using the Student ID.

### Display Subjects
Displays the subjects of a selected student.

### Exit
Stops the program with a thank-you message.

## Example of `match-case`

```python
match choice:
    case 1:
        # Add Student
    case 2:
        # Display All Students
    case 3:
        # Update Student
    case 4:
        # Delete Student
    case 5:
        # Display Subjects
    case 6:
        # Exit
    case _:
        print("Invalid choice.")
```

## Project Structure

```text
student-data-organizer/
│
├── main.py
└── README.md
```
# 📊 Student Record Structure

```python
{
    "Student ID":101,
    "Name":"Alice",
    "Age":20,
    "Grade":"B+",
    "DOB":"2002-05-14",
    "Subjects":[
        "Math",
        "Science",
        "English"
    ]
}
```

---

# ⚙ Program Workflow

```
Start
   │
   ▼

Display Menu

   │
   ▼

User Selects Option

   │

├── Add Student

├── Display Students

├── Update Student

├── Delete Student

├── Display Subjects

└── Exit

   │
   ▼

Repeat Until Exit
```

---
## 🎥 Project Demonstration
  <a href="YOUR_VIDEO_LINK">
    <img src="https://img.shields.io/badge/🎬%20Project%20Video-success?style=for-the-badge">
  </a>
</p>
---

## Why This Project Is Useful

This project is a good beginner-level Python program for learning:
- Dictionaries
- Loops
- User input handling
- CRUD operations
- `match-case` statements
- Menu-driven programming

## Future Improvements

- Save data permanently in a file or database.
- Add input validation.
- Allow searching students by name or grade.
- Store marks for each subject.
- Add a better GUI version.

# 📷 Screenshots of Output

<img width="853" height="445" alt="image" src="https://github.com/user-attachments/assets/59f2695b-b67a-485d-8d1e-fa1d7e819595" />
<img width="884" height="493" alt="image" src="https://github.com/user-attachments/assets/c52873c3-d977-47b8-a29d-c14d8b52bfa6" />



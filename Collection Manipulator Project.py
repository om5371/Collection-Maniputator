print("Welcome To The Student Data Organizer!")

students = {}
while True:
    print("\n===== Student Data Organizer =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            sid = input("Student ID: ")
            name = input("Name: ")
            age = input("Age: ")
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            subjects = input("Subjects (comma-separated): ")

            students[sid] = {
                "name": name,
                "age": age,
                "grade": grade,
                "dob": dob,
                "subjects": subjects
            }

            print("Student added successfully!")

        case 2:
            if len(students) == 0:
                print("No student found.")
            else:
                print("\n--- Student List ---")
                for sid, data in students.items():
                    print("Student ID:", sid)
                    print("Name:", data["name"])
                    print("Age:", data["age"])
                    print("Grade:", data["grade"])
                    print("DOB:", data["dob"])
                    print("Subjects:", data["subjects"])
                    print()

        case 3:
            sid = input("Enter Student ID to update: ")

            if sid in students:
                students[sid]["name"] = input("New Name: ")
                students[sid]["age"] = input("New Age: ")
                students[sid]["grade"] = input("New Grade: ")
                students[sid]["dob"] = input("New DOB: ")
                students[sid]["subjects"] = input("New Subjects: ")
                print("Student updated successfully!")
            else:
                print("Student not found.")

        case 4:
            sid = input("Enter Student ID to delete: ")

            if sid in students:
                del students[sid]
                print("Student deleted successfully!")
            else:
                print("Student not found.")

        case 5:
            sid = input("Enter Student ID: ")

            if sid in students:
                print("Subjects:", students[sid]["subjects"])
            else:
                print("Student not found.")

        case 6:
            print("Thank You!")
            break

        case _:
            print("Invalid choice.")
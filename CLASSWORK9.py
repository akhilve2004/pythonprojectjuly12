
class Student:

    students = []
    def add_student(self):
        roll = int(input("Enter Roll Number: "))
        for student in Student.students:
            if student[0] == roll:
                print("Student already exists!")
                return

        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        Student.students.append([roll, name, marks])
        print("Student added successfully!")
    def update_marks(self):
        roll = int(input("Enter Roll Number: "))

        for student in Student.students:
            if student[0] == roll:
                marks = float(input("Enter New Marks: "))
                student[2] = marks
                print("Marks updated successfully!")
                return

        print("Student not found!")
    def display_students(self):
        if len(Student.students) == 0:
            print("No student records found!")
        else:
            print("\nStudent Details")
            print("-----------------------")

            for student in Student.students:
                print("Roll No :", student[0])
                print("Name    :", student[1])
                print("Marks   :", student[2])
                print("-----------------------")
    def search_student(self):
        roll = int(input("Enter Roll Number: "))

        for student in Student.students:
            if student[0] == roll:
                print("\nStudent Found!")
                print("Roll No :", student[0])
                print("Name    :", student[1])
                print("Marks   :", student[2])
                return

        print("Student not found!")
    def delete_student(self):
        roll = int(input("Enter Roll Number: "))

        for student in Student.students:
            if student[0] == roll:
                Student.students.remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found!")


s = Student()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Display All Student Details")
    print("4. Search Student by Roll Number")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        s.add_student()

    elif choice == 2:
        s.update_marks()

    elif choice == 3:
        s.display_students()

    elif choice == 4:
        s.search_student()

    elif choice == 5:
        s.delete_student()

    elif choice == 6:
        print("Program exited.")
        break

    else:
        print("Invalid choice!")

# function for main menu
def show_menu():
    print("1. Insert New Record:\n"
          "2. View Overall Report:\n"
          "3. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        return None
    return choice


# function to add/insert new student record into students.txt file
def add_student(filename="students.txt"):
    name = input("Enter Student name: ")

    if student_exists(name, filename):
        print("Student already exists. Record not added!")
        return
    
    no_of_subjects = int(input("Enter number of subjects: "))
    marks = []

    for i in range(no_of_subjects):
        mark = int(input(f"Enter mark {i+1}: "))
        marks.append(str(mark))

    record = name + "," + ",".join(marks) + "\n"
    with open(filename, "a") as f:
        f.write(record)

    print("Record Saved")

def student_exists(name, filename="students.txt"):
    students = load_students(filename)
    if not students:
        return False
    
    for student in students:
        if(student["name"].lower() == name.lower()):
            return True
    return False

# function to read all student records
def load_students(filename="students.txt"):
    student_list = []

    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return None

    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        name = parts[0]
        marks = [int(m) for m in parts[1:]]
        student_list.append({"name": name, "marks": marks})

    return student_list


def compute_avg(marks):
    return sum(marks) / len(marks)


def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def find_topper(student_list):
    if not student_list:
        return None
    return max(student_list, key=lambda x: x["average"])


def print_report(student_list):
    top_student = find_topper(student_list)
    top_student_name = top_student["name"]
    top_avg = top_student["average"]

    print("\nStudent Performance Report")
    print("-" * 40)
    for student in student_list:
        print(f"{student['name']:10} | Avg: {student['average']:.1f} | Grade: {student['grade']}")

    print(f"\nTop Performer: {top_student_name} ({top_avg:.1f})\n")


# Main Loop
while True:
    choice = show_menu()

    if choice == 1:
        add_student()

    elif choice == 2:
        students = load_students()
        if not students:
            print("No student records found.")
            continue

        for student in students:
            avg = compute_avg(student["marks"])
            student["average"] = avg
            student["grade"] = assign_grade(avg)

        print_report(students)

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
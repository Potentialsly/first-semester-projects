students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    try:
        grade = float(input("Enter student grade: "))
    except ValueError:
        print("Invalid grade. Please enter a number.")
        return
    
    student = {
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(student)
    print(f"Student {name} added successfully!\n")

def view_students():
   if not students:
        print("No students in the system.\n")
        return

    print("\nList of Students:")
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
        print()

def get_average_grade():
    if not students:
        print("No student data to calculate average.\n")
        return

    total = sum(student['grade'] for student in students)
    average = total / len(students)
    print(f"Average Grade: {average:.2f}\n")
 

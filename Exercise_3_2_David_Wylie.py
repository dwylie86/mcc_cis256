# Your Name
# CIS256 Fall 2025
# EX 3.2
# Student Grade Program for Mr. Smarty and Dr. Devin Booker.
# Definitely NOT the grocery example repurposed ;)

# Student Grade Dictionary Key: Full Name, Value: Grade
student_grades = {
    "James Doe": "A",
    "Mary Jane": "B",
    "Alex Smith": "C",
    "Lisa Ray": "A",
    "John Green": "D",
    "Anna White": "B"
}

# Grade list to help Mr. Smarty if he enters invalid grade
possible_grades = ["a", "b", "c", "d", "f"]


def search_by_name(name):
    """
    Function to allow search of student grades dictionary by student name.
    :params: name: str - full name as it should appear in the dictionary.
    :return: None - prints student name and grade
    """
    formatted_name = name.title()
    if formatted_name in student_grades:
        print(
            f"{formatted_name} Grade: {student_grades[formatted_name]}"
            )
    else:
        print(
            "The student name entered does not exist."
            )


def search_by_grade(grade):
    """
    Function to allow search of student grades dictionary by letter grade.
    :params: name: str - letter grade confined to possible_grades list.
    :return: None - prints names with grade and count of students with grade.
    """
    students_by_grade = [
        student for student, letter in student_grades.items()
        if letter.lower() == grade.lower()
        ]
    if student_grades:
        print(f"Students with {grade.title()} Grade:")
        for student in students_by_grade:
            print(f"- {student}")
        print(
            f"Total students with {grade.title()} "
            f"Grade: {len(students_by_grade)}"
            )
    else:
        print("No students received the grade entered.")


while True:
    # Prompt Mr. Smarty to choose search by name or by grade
    choice = input(
        "Search by Name (N) or by Grade (G)? ").strip().upper()

    if choice == "N":
        # Search by student name
        name = input("Enter the student's name: ").strip()
        search_by_name(name)
    elif choice == "G":
        # Search by grade
        grade = input("Enter the grade: ").strip()
        if grade.lower() in possible_grades:
            search_by_grade(grade)
        else:
            print("Please enter A, B, C, D, or F")

    else:
        print(
            "Invalid option. Please enter 'N' for Item Name or "
            "'G' for Grade."
            )

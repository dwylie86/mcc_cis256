# David Wylie
# CIS256 24903
# Programming Assignment 3 (PA 3)
# Execise 1: List Manipulation
# I reused logic from the EMS program from last week

class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __str__(self):
        return f"{self.name}"


class Student_List:
    def __init__(self):
        self._student_list = []

    def __len__(self):
        # Dunder Method to add len attribute to class
        return len(self._student_list)

    def add_student(self, name):
        """
        Method to add a new student object to student list
        :params: name: str - name of student
        :return: None, appends student list
        """
        formatted_name = name.title()
        new_student = Student(formatted_name)
        self._student_list.append(new_student)
        print(f"\n{formatted_name} was added to the list\n")

    def remove_student(self, name):
        """
        Method to remove an existing student object in the student list
        :params: name - used to find student object
        :return: None, removes student object
        """
        formatted_name = name.title()
        for student in self._student_list:
            if student.name == formatted_name:
                self._student_list.remove(student)
                print(f"\n{formatted_name} was removed from the list\n")
                return

        print("Student not found")

    def select_student_slice(self, first, last):
        """
        Method to return a slice of the student list
        :params: first: int - starting position (1-indexed)
        :params: last: int - ending position (inclusive)
        :return: str - formatted string of selected students
        """
        if first < 1 or last > len(self._student_list) or last < first:
            return (
                f"Invalid range, select between 1 and "
                f"{len(self._student_list)}"
            )
        sliced_list = self._student_list[first - 1:last]
        students = '\n'.join(
            f"{i}. {student}" for i, student in enumerate(sliced_list, 1)
            )
        return (
            f"Student List: {len(sliced_list)} Students\n{'-' * 16}\n"
            f"{students}\n"
        )

    def __str__(self):
        if not self._student_list:
            return "Student List: 0 Students\n(empty)\n"
        students = '\n'.join(
            f"{i}. {student}" for i, student in enumerate(self._student_list, 1)
            )
        return (
            f"Student List: {len(self._student_list)} Students\n"
            f"{'-' * 16}\n{students}\n"
        )


def user_interface(student_list):
    """
        Helper function to interact with student objects in the
        student list object
        :params: Student list object
        :return: None, Uses all helper functions to interact with student list
    """
    # Main program loop - continues until user chooses to exit
    while True:
        try:
            print("""Select from the Following Options
    1. View all Students
    2. Display a Slice of Students
    3. Add a Student
    4. Remove an Existing Student
    5. Exit Application
                  """)

            response = int(input("Enter Option: "))
            match response:
                case 1:
                    print(student_list)
                case 2:
                    if len(student_list) == 0:
                        print(student_list)
                    else:
                        first = (
                            int(input("Select First Student Number (>=1): "))
                        )
                        last = (
                            int(input(f"Select Last Student Number (Between "
                                      f"{first} and {len(student_list)}): "))
                        )
                        print(
                            f"\n{student_list.select_student_slice(
                                first, last
                                )}"
                            )
                case 3:
                    student_list.add_student(
                        str(input("Please enter student's Name: "))
                    )
                case 4:
                    student_list.remove_student(
                        str(input("Please enter student's Name: "))
                    )
                case 5:
                    print("Goodbye!")
                    exit()
                case _:
                    print("Please Enter a Number from 1 to 5.")
        except ValueError:
            print("Error: Please enter a valid integer.")


student_list = Student_List()

# Some debug code to add students to the list
# student_list.add_student("alice")
# student_list.add_student("BRYCE")
# student_list.add_student("CaLVin")
# student_list.add_student("Frank")
# student_list.add_student("STefanie")


def main():
    print("---Welcome to the Student List Management System---")
    if len(student_list) == 0:
        first_student = (
            str(input("Please add a student to the list to get started: "))
            )
        student_list.add_student(first_student)
        user_interface(student_list)
    else:
        user_interface(student_list)


main()

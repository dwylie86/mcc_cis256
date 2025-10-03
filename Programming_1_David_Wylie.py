# David Wylie
# CIS256 24903
# Programming Assignment 1 (PA2)
# Employee Management System (EMS)
# An employee management system where you can
# add new employees, update their information,
# view all employee details, and delete records.

class Employee:
    def __init__(self, name, salary, employee_id):
        self._name = name
        self._salary = salary
        self._employee_id = employee_id

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @property
    def employee_id(self):  # read-only
        return self._employee_id

    @name.setter
    def name(self, value):
        self._name = value

    @salary.setter
    def salary(self, value):
        self._salary = value

    def __str__(self):
        return f"Employee({self.name}, ${self.salary}, ID: {self.employee_id})"


class EMS:
    def __init__(self):
        self._employees = []

    def get_employee(self, employee_id):
        """
        Method to return an employee object for manipulation
        and maintain encapsulation
        :params: employee_id - the employee id of the object
        :return: an employee object to work with or None
        """
        for emp in self._employees:
            if emp.employee_id == employee_id:
                return emp
        return None

    def get_next_id(self):
        """
        Method to return the next, unused, employee id in series
        to maintain encapsulation and unique ids
        :params: self
        :return: int, next id in series
        """
        last_id = 0
        # Iterate through all employees to find the highest existing ID
        for emp in self._employees:
            if emp.employee_id > last_id:
                last_id = emp.employee_id
        return last_id + 1

    def has_employees(self):
        """
        Method to check if the employee list has employees
        Necessary logic checks for EMS functions.
        :params: self
        :return: length of _employees list
        """
        return len(self._employees) > 0

    def add_employee(self, name, salary, employee_id=None):
        """
        Method to add a new employee object to employee list
        :params: name: str - name of employee
                 salary: int - salary of employee
                 employee_id int - employee id, auto generated
        :return: None, appends employee list
        """
        new_employee = Employee(name, salary, employee_id)
        self._employees.append(new_employee)

    def update_employee(self, employee_id, name, salary):
        """
        Method to update an existing employee object in the employee list
        :params: name: str - name of employee
                 salary: int - salary of employee
                 employee_id int - employee id, used to find employee object
        :return: None, updates employee object attributes
        """
        employee_update = self.get_employee(employee_id)
        employee_update.name = name
        employee_update.salary = salary

    def remove_employee(self, employee_id):
        """
        Method to remove an existing employee object in the employee list
        :params: employee_id int - employee id, used to find employee object
        :return: None, updates employee object attributes
        """
        emp = self.get_employee(employee_id)
        if emp:
            self._employees.remove(emp)
        else:
            print("Employee not found")

    def view_employee(self, employee_id):
        """
        Method to view an existing employee object in the employee list
        :params: employee_id int - employee id, used to find employee object
        :return: None, displays employee object and attributes
        """
        emp = self.get_employee(employee_id)
        if emp:
            print(f"{'Employee Name':<20} {'Salary':>12} {'ID':>5}")
            print("-" * 40)
            print(f"{emp.name:<20} ${emp.salary:>10,} {emp.employee_id:>5}")
        else:
            print("No Employees Found in EMS.")

    def view_all_employees(self):
        """
        Method to view all existing employee objects in the employee list
        :params: Self
        :return: None, displays all employee objects and attributes
        """
        print(f"{'Employee Name':<20} {'Salary':>12} {'ID':>5}")
        print("-" * 40)
        for emp in self._employees:
            print(
                f"{emp.name:<20} ${emp.salary:>10,} {emp.employee_id:>5}"
                )


def validate_id(business):
    """
        Helper function to find a valid employee ID
        :params: EMS Object
        :return: int -
                    employee_id attribute of the employee object in EMS object
    """
    while True:
        try:
            employee_id = int(input("Enter ID: "))

            if business.get_employee(employee_id) is not None:
                return employee_id
            else:
                print(
                    f"Error: Employee with ID {employee_id} not found. "
                    f"Please try again."
                )

        except ValueError:
            print("Error: Please enter a valid integer.")


def validate_salary(optional=False):
    """
        Helper function to ensure valid entry to
        salary attribute of employee object
        :params: Optonal Flag - Allows to skip (Update Function)
        :return: int - Validated salary amount
    """
    while True:
        # Build appropriate prompt based on optional flag
        prompt = (
            "Enter Salary (or press Enter to skip): "
            if optional else "Enter Salary: "
        )
        salary_input = input(prompt)

        if optional and not salary_input:
            return None

        try:
            salary = int(salary_input)
            if salary > 0:
                return salary
            else:
                print("Error: Salary must be positive and greater than zero.")
        except ValueError:
            print("Error: Please enter a valid integer.")


def validate_name(optional=False):
    """
        Helper function to ensure valid entry to
        name attribute of employee object
        :params: Optonal Flag - Allows to skip (Update Function)
        :return: str - Validated string for name attribute of employee object
    """
    while True:
        # Build appropriate prompt based on optional flag
        prompt = (
            "Enter Name (or press Enter to skip): "
            if optional else "Enter Name: "
        )
        name = input(prompt)

        if optional and (not name or name.isspace()):
            return None

        if not optional and (not name or name.isspace()):
            print("Error: Name cannot be empty. Please try again.")
            continue

        if any(char.isdigit() for char in name):
            print("Error: Name cannot contain numbers. Please try again.")
            continue

        return name


def handle_view_employee(business):
    """
        Helper function to view an employee object in the
        employee list of the EMS Object
        :params: EMS Object
        :return: None, displays employee object and attributes
    """
    print("\n---View Employee---")
    if not business.has_employees():
        print("No employees to view.")
        return
    employee_id = validate_id(business)
    business.view_employee(employee_id)


def handle_view_all_employees(business):
    """
        Helper function to view all employee objects in the
        employee list of the EMS Object
        :params: EMS Object
        :return: None, displays employee object and attributes
    """
    print("\n---View All Employees---")
    if not business.has_employees():
        print("No employees to view.")
        return
    business.view_all_employees()


def handle_update_employee(business):
    """
        Helper function to make updates to employee objects in the
        employee list of the EMS Object
        :params: EMS Object
        :return: None, updates object attributes in EMS object employee list
    """
    print("\n---Update Employee---")
    if not business.has_employees():
        print("No employees to view.")
        return
    employee_id = validate_id(business)

    emp = business.get_employee(employee_id)
    print(f"Current: {emp.name}, ${emp.salary}")

    new_name = validate_name(optional=True)
    new_salary = validate_salary(optional=True)
    if new_name is not None:
        emp.name = new_name
    if new_salary is not None:
        emp.salary = new_salary
    print("Employee updated!")


def handle_add_employee(business):
    """
        Helper function to add employee objects in the
        employee list of the EMS Object
        :params: EMS Object
        :return: None, adds employee object EMS object employee list
    """
    print("\n---Add New Employee---")
    next_id = business.get_next_id()
    add_name = validate_name()
    add_salary = validate_salary()
    business.add_employee(add_name, add_salary, next_id)


def handle_remove_employee(business):
    """
        Helper function to remove employee objects in the
        employee list of the EMS Object
        :params: EMS Object
        :return: None, removes employee object EMS object employee list
    """
    print("\n---Remove Employee---")
    if not business.has_employees():
        print("No employees to view.")
        return
    employee_id = validate_id(business)
    business.remove_employee(employee_id)


def user_interface(business):
    """
        Helper function to interact with employee objects in the
        employee list of the EMS Object
        :params: EMS Object
        :return: None, Uses all helper functions to interact with EMS object
    """
    print("---Welcome to the Employee Management System---")
    # Main program loop - continues until user chooses to exit
    while True:
        try:
            print("""
Select from the Following Options
    1. View an employee
    2. View all employees
    3. Add New Employee
    4. Update Existing Employee
    5. Remove Existing Employee
    6. Exit Application
                  """)

            response = int(input("Enter Option: "))
            match response:
                case 1:
                    handle_view_employee(business)
                case 2:
                    handle_view_all_employees(business)
                case 3:
                    handle_add_employee(business)
                case 4:
                    handle_update_employee(business)
                case 5:
                    handle_remove_employee(business)
                case 6:
                    print("Goodbye!")
                    exit()
                case _:
                    print("Please Enter a Number from 1 to 6.")
        except ValueError:
            print("Error: Please enter a valid integer.")


def main():
    """
        Main Entry Point of the program
    """
    # Initialize the Employee Management System
    business = EMS()

    # DEBUG DATA - Uncomment below lines to view in EMS
    # business.add_employee("Alice", 50000, 1)
    # business.add_employee("Alice Two", 60000, 2)
    # business.add_employee("Alice Three", 70000, 3)
    # business.add_employee("Alice Four", 80000, 4)

    # Check if system is empty and prompt for first employee
    if not business.has_employees():
        print(
            "No Employees Found in EMS. "
            "Please add an employee to get started."
            )
        handle_add_employee(business)
    # Start the main user interface
    user_interface(business)


main()

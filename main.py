import json

# Employee class to represent individual employees
class Employee:
    def __init__(self, name, emp_id, title, department):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Title: {self.title}, Department: {self.department}")

    def __str__(self):
        return f"{self.name} - ID: {self.emp_id}"

# Department class to represent departments containing employees
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                print(f"Employee with ID {emp_id} removed from {self.name}")
                return
        print(f"Employee with ID {emp_id} not found in {self.name}")

    def list_employees(self):
        print(f"Employees in department {self.name}:")
        for employee in self.employees:
            print(employee)

# Company class to manage departments and employees
class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department):
        self.departments[department.name] = department

    def remove_department(self, department_name):
        if department_name in self.departments:
            del self.departments[department_name]
            print(f"Department {department_name} removed.")
        else:
            print(f"Department {department_name} not found.")

    def display_departments(self):
        print("List of departments:")
        for department_name in self.departments:
            print(department_name)

    def list_all_departments_with_employees(self):
        print("Department-wise employee list:")
        for department_name, department in self.departments.items():
            print(f"\nDepartment: {department_name}")
            department.list_employees()

# Function to save company data to a JSON file
def save_company_data(company):
    with open("company_data.json", "w") as file:
        data = {
            "departments": {
                department.name: [emp.__dict__ for emp in department.employees]
                for department in company.departments.values()
            }
        }
        json.dump(data, file, indent=4)

# Function to load company data from a JSON file
def load_company_data():
    try:
        with open("company_data.json", "r") as file:
            try:
                data = json.load(file)
                company = Company()
                for department_name, employees in data["departments"].items():
                    department = Department(department_name)
                    for emp_data in employees:
                        employee = Employee(emp_data["name"], emp_data["emp_id"], emp_data["title"], emp_data["department"])
                        department.add_employee(employee)
                    company.add_department(department)
                return company
            except ValueError as e:
                raise ValueError("Employee name cannot be empty")
    except FileNotFoundError:
        return Company()

# Function to display menu options
def display_menu():
    print("\nEmployee Management System Menu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. List Employees in Department")
    print("4. Add Department")
    print("5. Remove Department")
    print("6. Display Departments")
    print("7. List All Departments with Employees")
    print("8. Exit")

def main():
    company = load_company_data()

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            try:
                name = input("Enter employee name: ")
                if not name:
                    raise ValueError("Employee name cannot be empty")
                
                emp_id = input("Enter employee ID: ")
                if not emp_id:
                    raise ValueError("Employee ID cannot be empty")
                
                title = input("Enter employee title: ")
                if not title:
                    raise ValueError("Employee title cannot be empty")
                
                department = input("Enter department name: ")
                if not department:
                    raise ValueError("Department name cannot be empty")
                try:
                    if department in company.departments:
                        employee = Employee(name, emp_id, title, department)
                        company.departments[department].add_employee(employee)
                        print("Employee added successfully.")
                    else:
                        raise KeyError("Department does not exist.")
                except KeyError as e:
                    print(f"Error: {e}")
            except ValueError as e:
                print(f"Exception caught - {e}")
                raise ValueError("Employee name exceeds maximum length")

        elif choice == "2":
            emp_id = input("Enter employee ID to remove: ")
            for department in company.departments.values():
                department.remove_employee(emp_id)
        elif choice == "3":
            department_name = input("Enter department name to list employees: ")
            if department_name in company.departments:
                company.departments[department_name].list_employees()
            else:
                print("Department does not exist.")
        elif choice == "4":
            department_name = input("Enter new department name: ")
            department = Department(department_name)
            company.add_department(department)
            print("Department added successfully.")
        elif choice == "5":
            department_name = input("Enter department name to remove: ")
            company.remove_department(department_name)
        elif choice == "6":
            company.display_departments()
        elif choice == "7":
            company.list_all_departments_with_employees()
        elif choice == "8":
            save_company_data(company)
            print("Exiting program. Company data saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()

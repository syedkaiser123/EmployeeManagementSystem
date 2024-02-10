import unittest
from unittest.mock import patch
from main import Employee, Department, Company

# Test adding an employee to a department
def test_add_employee():
    department = Department("Engineering")
    employee = Employee("John Doe", "EMP001", "Software Engineer", "Engineering")
    department.add_employee(employee)
    assert employee in department.employees

# Test removing an employee from a department
def test_remove_employee():
    department = Department("Engineering")
    employee = Employee("John Doe", "EMP001", "Software Engineer", "Engineering")
    department.add_employee(employee)
    department.remove_employee("EMP001")
    assert employee not in department.employees

# Test adding a department to a company
def test_add_department():
    company = Company()
    department = Department("Engineering")
    company.add_department(department)
    assert "Engineering" in company.departments

# Test removing a department from a company
def test_remove_department():
    company = Company()
    department = Department("Engineering")
    company.add_department(department)
    company.remove_department("Engineering")
    assert "Engineering" not in company.departments

# Test listing employees in a department
def test_list_employees_in_department(capfd):
    department = Department("Engineering")
    employee1 = Employee("John Doe", "EMP001", "Software Engineer", "Engineering")
    employee2 = Employee("Jane Smith", "EMP002", "Data Scientist", "Engineering")
    department.add_employee(employee1)
    department.add_employee(employee2)
    department.list_employees()
    out, _ = capfd.readouterr()
    expected_output = "Employees in department Engineering:\nJohn Doe - ID: EMP001\nJane Smith - ID: EMP002\n"
    assert out == expected_output

# Test listing all departments with employees
def test_list_all_departments_with_employees(capfd):
    company = Company()
    department1 = Department("Engineering")
    department2 = Department("HR")
    company.add_department(department1)
    company.add_department(department2)
    employee1 = Employee("John Doe", "EMP001", "Software Engineer", "Engineering")
    employee2 = Employee("Jane Smith", "EMP002", "HR Manager", "HR")
    department1.add_employee(employee1)
    department2.add_employee(employee2)
    company.list_all_departments_with_employees()
    out, _ = capfd.readouterr()
    expected_output = (
        "Department-wise employee list:\n\n"
        "Department: Engineering\n"
        "Employees in department Engineering:\n"
        "John Doe - ID: EMP001\n\n"
        "Department: HR\n"
        "Employees in department HR:\n"
        "Jane Smith - ID: EMP002\n"
    )
    assert out == expected_output


# Employee Management System

The Employee Management System is a command-line application written in Python. It allows users to manage employees and departments within a company.

## Features

- Add and remove employees
- List employees in a department
- Add and remove departments
- Display a list of all departments with their employees
- Save and load company data to/from a JSON file

## Installation

1. Clone the repository: `git clone https://github.com/syedkaiser123/EmployeeManagementSystem.git` 
2. Navigate to the project directory: `cd EmployeeManagementSystem`

## Usage
1. Run the application: `python main.py`

2. Follow the below steps:
    - Choose option 4 to add departments one after another.
    - Then choose option 1 to add employees to the departments of your choice from the available ones. You can use option 6 to display all the available departments.
    - Option 2 can be used to remove an employee.
    - Option 3 can be used to list employees of a particular department.
    - Option 6 can be used to remove a department.
    - Option 7 can be used to list all the departments with their corresponding employees.

3. Choose option 8 to exit the program. Your company data will be saved automatically to `company_data.json` in the project directory.

4. Any other options chosen when prompted for one, will be discarded with an error message as `Invalid choice. Please enter a number between 1 and 8.`

## File Structure

- `main.py`: Main Python script containing the application logic.
- `company_data.json`: JSON file used to store company data.
- `README.md`: Documentation file.



# Define the database as a list
employee_database = []

# Function to add an employee to the database
def add_employee(employee_id, name, job_title):
    employee_entry = (employee_id, name, job_title)
    employee_database.append(employee_entry)
    print(f"Employee {name} added to the database.")

# Function to display all employees in the database
def display_employees():
    print("\nEmployee Database:")
    for employee in employee_database:
        print(f"ID: {employee[0]}, Name: {employee[1]}, Job Title: {employee[2]}")

# Example: Adding employees to the database
add_employee(1, "Prerit", "Software Engineer")
add_employee(2, "Ishan", "Data Scientist")

# Displaying the contents of the database
display_employees()

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        print("Role: Manager")

class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")
        print("Role: Developer")

# Example Usage
if __name__ == "__main__":
    # Creating instances of the classes
    emp1 = Manager("Sachin", 102, 80000, "IT")
    emp2 = Developer("Ishan", 103, 700000, "Python")

    # Displaying information
    print("Manager Information:")
    emp1.display_info()
    print("\nDeveloper Information:")
    emp2.display_info()

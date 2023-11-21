# Function to create a new student record
def create_student_record(name, age, grade):
    return {"Name": name, "Age": age, "Grade": grade}

# Function to search for a student by name
def search_student(records, name):
    for record in records:
        if record["Name"].lower() == name.lower():
            return record
    return None

# Main program
if __name__ == "__main__":
    # List to store student records
    student_records = []

    # Adding some sample records
    student_records.append(create_student_record("Ishan", 18, "A"))
    student_records.append(create_student_record("Sachin", 17, "B"))
    student_records.append(create_student_record("Prerit", 19, "C"))

    # Taking user input to search for a student
    search_name = input("Enter the name of the student you want to search: ")

    # Searching for the student
    result = search_student(student_records, search_name)

    # Displaying the result
    if result:
        print("Student Found:")
        print("Name:", result["Name"])
        print("Age:", result["Age"])
        print("Grade:", result["Grade"])
    else:
        print("Student not found.")

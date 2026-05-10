# Week 6 Assignment - Loops, User Input, and Comprehensions
# This program gathers employee information with validation,
# stores it in a list of dictionaries, and updates the data using comprehensions.


# Create an empty list that will hold all employee dictionaries
employee_list = []

# Define the characters that are NOT allowed in the email field
invalid_email_chars = ['!', '"', "'", '#', '$', '%', '^', '&', '*', '(', ')',
                       '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']',
                       '{', '}', '\\']

# Define the characters that are NOT allowed in the address field
invalid_address_chars = ['!', '"', "'", '@', '$', '%', '^', '&', '*', '_',
                         '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}']

# Define allowed special characters for the name field
allowed_name_chars = [' ', "'", '-']


# Start the main loop - keep asking for employees until the user says no
while True:

    # ---------- EMPLOYEE ID ----------
    # ID is required, must be a number that is 7 digits or less
    while True:
        emp_id = input("Enter Employee ID (number, 7 digits or less): ")

        # Check if the user entered something
        if emp_id == "":
            print("Employee ID is required. Please try again.")
            continue

        # Check if the ID is all digits and 7 or less characters
        if emp_id.isdigit() and len(emp_id) <= 7:
            # Convert to a number and exit this loop
            emp_id = int(emp_id)
            break
        else:
            print("Invalid ID. Must be a number with 7 digits or less.")


    # ---------- EMPLOYEE NAME ----------
    # Name is required, must be letters, spaces, apostrophes, or hyphens
    while True:
        emp_name = input("Enter Employee Name: ")

        # Check if user entered something
        if emp_name == "":
            print("Employee Name is required. Please try again.")
            continue

        # Check each character in the name to make sure it is valid
        name_is_valid = True
        for char in emp_name:
            if not char.isalpha() and char not in allowed_name_chars:
                name_is_valid = False
                break

        if name_is_valid:
            break
        else:
            print("Invalid Name. Only letters, spaces, ' and - are allowed.")


    # ---------- EMPLOYEE EMAIL ----------
    # Email is required, must be mostly alphanumeric, no special invalid chars
    while True:
        emp_email = input("Enter Employee Email Address: ")

        # Check if user entered something
        if emp_email == "":
            print("Employee Email is required. Please try again.")
            continue

        # Check if the email contains any of the invalid characters
        email_is_valid = True
        for char in emp_email:
            if char in invalid_email_chars:
                email_is_valid = False
                break

        if email_is_valid:
            break
        else:
            print("Invalid Email. It contains characters that are not allowed.")


    # ---------- EMPLOYEE ADDRESS ----------
    # Address is NOT required, but if given it must follow rules
    while True:
        emp_address = input("Enter Employee Address (optional, press Enter to skip): ")

        # If the user skipped it, that is okay
        if emp_address == "":
            break

        # Check if the address contains any invalid characters
        address_is_valid = True
        for char in emp_address:
            if char in invalid_address_chars:
                address_is_valid = False
                break

        if address_is_valid:
            break
        else:
            print("Invalid Address. It contains characters that are not allowed.")


    # ---------- EMPLOYEE SALARY ----------
    # Salary is required, must be a float between 18 and 27
    while True:
        emp_salary = input("Enter Employee Salary (between 18 and 27): ")

        # Check if user entered something
        if emp_salary == "":
            print("Employee Salary is required. Please try again.")
            continue

        # Try to convert to a float, and check the range
        try:
            emp_salary = float(emp_salary)
            if emp_salary >= 18 and emp_salary <= 27:
                break
            else:
                print("Salary must be between 18 and 27.")
        except ValueError:
            print("Invalid Salary. Please enter a number.")


    # ---------- BUILD THE DICTIONARY AND ADD TO LIST ----------
    # Put all the collected info into a dictionary
    employee = {
        "id": emp_id,
        "name": emp_name,
        "email": emp_email,
        "address": emp_address,
        "salary": emp_salary
    }

    # Add the dictionary to our main list
    employee_list.append(employee)
    print("Employee added successfully!\n")


    # ---------- ASK IF USER WANTS TO ADD ANOTHER ----------
    while True:
        another = input("Do you want to add another employee? (yes/no): ").lower()
        if another == "yes" or another == "y":
            break  # break inner loop, outer loop will continue
        elif another == "no" or another == "n":
            break  # break inner loop, then we will break outer loop
        else:
            print("Please enter yes or no.")

    # If user said no, exit the main loop
    if another == "no" or another == "n":
        break


# ---------- USE COMPREHENSIONS TO UPDATE THE LIST ----------

# Comprehension 1: Add "IT Department" to each employee's name
employee_list = [
    {**emp, "name": emp["name"] + " IT Department"}
    for emp in employee_list
]

# Comprehension 2: Increase salary by 30% to include benefits
employee_list = [
    {**emp, "salary": emp["salary"] * 1.30}
    for emp in employee_list
]


# ---------- PRINT THE UPDATED LIST ----------
print("\n--- Updated Employee List ---")
for emp in employee_list:
    print(emp)

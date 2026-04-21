# Walsh College - Python Assignment
# Author: Umer Khatab

import math  # Needed for math.sqrt() in Step 12


# --- Step 1: Store first name as a variable in all lowercase ---
first_name = "umer"

# --- Step 2: Store last name as a variable in all uppercase ---
last_name = "KHATAB"

# --- Step 3: Print "Hello, <first name upper> <last name lower>" using string functions ---
print("Hello, " + first_name.upper() + " " + last_name.lower())

# --- Step 4: Print two newlines ---
print("\n")

# --- Step 5: New variable storing first and last name together with a space between ---
full_name = first_name + " " + last_name

# --- Step 6: Slice the last name out of the variable from Step 5 and print it (on one line) ---
print(full_name[len(first_name) + 1:])

# --- Step 7: Replace the last name with "<last name>, Walsh College Student" and print ---
full_name = full_name.replace(last_name, last_name + ", Walsh College Student")
print(full_name)

# --- Step 8: Print the quote with quotation marks at the beginning and end of the output ---
print("\"Start by doing what's necessary; then do what's possible; "
      "and suddenly you are doing the impossible - Francis of Assisi\"")

# --- Step 9: Store 2 decimal numbers as variables ---
num1 = 15.5
num2 = 4.2

# --- Step 10: Store add, subtract, multiply, and divide operations as variables ---
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# --- Step 11: Print each result using a DIFFERENT technique for each line ---

# Technique 1: String concatenation
print(str(num1) + " plus " + str(num2) + " equals " + str(addition))

# Technique 2: String formatting expression (% operator)
print("%s minus %s equals %s" % (num1, num2, subtraction))

# Technique 3: String .format() method call
print("{} times {} equals {}".format(num1, num2, multiplication))

# Technique 4: f-String
print(f"{num1} divided by {num2} equals {division}")

# --- Step 12: sq_root = square root of multiplication, rounded to 2 decimals ---
sq_root = round(math.sqrt(multiplication), 2)
print("The square root of {} equals {}".format(multiplication, sq_root))

# --- Step 13: Store the current month as a string and the day of the month as a number ---
month = "April"
day = 21

# --- Step 14: Print the day/month sentence on a new line, tabbed over twice ---
# (Using an f-string here, a different technique than the .format() used in Step 12)
print(f"\n\t\tToday is day {day} of the month of {month}.")

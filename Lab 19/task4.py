def print_students(students):
    print("\n--- Python Output ---")
    print("Student List:")
    # Using a for...in loop for clean iteration over list elements
    for name in students:
        print(name)
# Test with sample student names
student_list = ["Alice", "Bob", "Charlie", "Diana"]
print_students(student_list)
# --- Dynamic Input Section (Adding a Student) ---
print("\n--- Dynamic Input Test (Adding a Student) ---")
try:
    # Get dynamic input from the user
    new_student = input("Enter a new student name to add to the list: ")
    # Add the new name to the existing list
    student_list.append(new_student)
    # Call the function again with the updated list
    print_students(student_list)
except Exception as e:
    print(f"An error occurred: {e}")
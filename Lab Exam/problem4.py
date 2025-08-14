def generate_emails(student_names):
    emails = []
    for name in student_names:
        parts = name.strip().split()
        if len(parts) == 1:
            email = parts[0].lower() + "@sru.edu.in"
        else:
            first = parts[0].lower()
            last = parts[-1].lower()
            email = first + last + "@sru.edu.in"
        emails.append(email)
    return emails

# Example usage:
students = []
n = int(input("Enter number of students: "))
for _ in range(n):
    name = input("Enter student name: ")
    students.append(name)

emails = generate_emails(students)
for email in emails:
    print(email)
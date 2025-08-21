class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print(f"Student Name : {self.name}")
        print(f"Roll Number  : {self.roll_no}")
        print(f"Marks        : {self.marks}")
        print(f"Grade        : {self.calculate_grade()}")

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "Fail"


# --------- Taking Dynamic Input ---------
name = input("Enter Student Name: ")
roll_no = int(input("Enter Roll Number: "))
marks = float(input("Enter Marks: "))

student = Student(name, roll_no, marks)
print("\n--- Student Details ---")
student.display_details()

class Student:
    """
    Represents a student with a name, age, and a list of marks.
    
    Methods:
        show_details(): Prints the student's name and age.
        total_marks(): Returns the total of all marks.
    """

    def __init__(self, name, age, marks):
        """
        Initializes a Student instance.

        Args:
            name (str): The student's name.
            age (int): The student's age.
            marks (list of int/float): List of marks in subjects.
        """
        self.name = name
        self.age = age
        self.marks = marks

    def show_details(self):
        """Displays the student's name and age."""
        print(f"Name: {self.name}, Age: {self.age}")

    def total_marks(self):
        """Calculates and returns the total marks."""
        return sum(self.marks)
# Example usage:
student = Student("Alice", 20, [85, 90, 78])
student.show_details()
print(f"Total Marks: {student.total_marks()}")

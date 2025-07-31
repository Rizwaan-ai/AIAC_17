class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        for attr, value in self.__dict__.items():
            print(f"{attr.capitalize()}: {value}")

    @classmethod
    def from_input(cls):
        name = input("Enter name: ")
        rollno = int(input("Enter roll number: "))
        marks = float(input("Enter marks: "))
        return cls(name, rollno, marks)

# Example usage
if __name__ == "__main__":
    s = Student.from_input()
    s.display()
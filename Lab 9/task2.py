class sru_student:
    """
    A class to represent a student at SRU.
    Attributes:
        name (str): The name of the student.
        roll_no (str): The roll number of the student.
        hostel_status (str): The hostel accommodation status of the student.
        fee_paid (bool): Indicates whether the student's fee has been paid.
    Methods:
        fee_update(status):
            Updates the fee payment status of the student.
        display_details():
            Prints the details of the student, including name, roll number, hostel status, and fee payment status.
    """
    def __init__(self, name, roll_no, hostel_status):
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee_paid = False

    def fee_update(self, status):
        self.fee_paid = status

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No.: {self.roll_no}")
        print(f"Hostel Status: {self.hostel_status}")
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")


# Example usage:
if __name__ == "__main__":
    student1 = sru_student("Amit Kumar", "SRU123", "Hosteller")
    student1.fee_update(True)
    student1.display_details()
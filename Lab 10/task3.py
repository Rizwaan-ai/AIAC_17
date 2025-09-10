class Employee:
    def __init__(self, name, salary):     
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):             
        self.salary += self.salary * percent / 100

    def print_info(self):               
        print(f"Employee: {self.name}, Salary: {self.salary}")

def main():
    employees = [
        ("Shayla", 50000, 10),
        ("Isabel", 60000, 5),
        ("Taylor", 70000, 20)
    ]
    for name, salary, percent in employees:
        emp = Employee(name, salary)
        emp.increase_salary(percent)
        emp.print_info()

if __name__ == "__main__":
    main()
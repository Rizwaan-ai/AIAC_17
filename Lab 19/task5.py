class Car:
    # Constructor method (__init__)
    def __init__(self, brand, model, year):
        # Attributes are created and initialized here
        self.brand = brand
        self.model = model
        self.year = year
    # Method to display details
    def display_details(self):
        print("--- Python Output ---")
        print("Car Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
# --- Object Creation and Method Call ---
# 1. Create an object (instance of the Car class)
my_python_car = Car("Toyota", "Corolla", 2020)
# 2. Call the method
my_python_car.display_details()
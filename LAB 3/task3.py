
units = float(input("Enter the number of units consumed: "))
cost_per_unit = float(input("Enter the cost per unit: "))

# Calculate total bill
total_bill = units * cost_per_unit

# Display the result
print(f"Total electricity bill: {total_bill}")
def calculate_bill(units, cost_per_unit):
    """
    Calculate the total electricity bill.
    """
    return units * cost_per_unit

def print_decorative_bill(units, cost_per_unit, total_bill):
    """
    Print a decorative end bill after payment.
    """
    print("\n" + "="*35)
    print("         ELECTRICITY BILL")
    print("="*35)
    print(f"Units Consumed   : {units}")
    print(f"Cost per Unit    : {cost_per_unit}")
    print("-"*35)
    print(f"Total Bill       : {total_bill}")
    print("="*35)
    print("   Thank you for your payment!")
    print("="*35)

# Use the functions
total_bill = calculate_bill(units, cost_per_unit)

# Simulate payment (for demonstration, just ask user to press Enter)
input("\nPress Enter to make payment...")

# Print the decorative bill
print_decorative_bill(units, cost_per_unit, total_bill)
# Menu-driven program to show previous bill details and calculate new bill

# Store previous bills in a list
previous_bills = []

def show_previous_bills():
    if not previous_bills:
        print("\nNo previous bills found.")
    else:
        print("\n" + "="*35)
        print("        PREVIOUS BILL DETAILS")
        print("="*35)
        for idx, bill in enumerate(previous_bills, 1):
            print(f"Bill {idx}: Units={bill['units']}, Cost/Unit={bill['cost_per_unit']}, Total={bill['total_bill']}")
        print("="*35)

while True:
    print("\nMenu:")
    print("1. Calculate new electricity bill")
    print("2. Show previous bill details")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        try:
            units = float(input("Enter the number of units consumed: "))
            cost_per_unit = float(input("Enter the cost per unit: "))
            total_bill = calculate_bill(units, cost_per_unit)
            input("\nPress Enter to make payment...")
            print_decorative_bill(units, cost_per_unit, total_bill)
            # Save this bill to previous_bills
            previous_bills.append({
                'units': units,
                'cost_per_unit': cost_per_unit,
                'total_bill': total_bill
            })
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    elif choice == '2':
        show_previous_bills()
    elif choice == '3':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

from datetime import datetime

def convert_date_format(date_str):
    """
    Converts a date string from 'YYYY-MM-DD' to 'DD-MM-YYYY' format.
    """
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%d-%m-%Y")

def main():
    # Example usage:
    print(convert_date_format("2023-10-15"))  # Output: "15-10-2023"

if __name__ == "__main__":
    main()

def format_name(name):
    parts = name.strip().split()
    if len(parts) < 2:
        return name  # Return as is if there's only one part
    # Move the last part to the front, rest to the back
    return f"{parts[-1]} {' '.join(parts[:-1])}"

if __name__ == "__main__":
    input_name = input("Enter a name: ")
    print(format_name(input_name))
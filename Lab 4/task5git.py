import os

def count_lines_in_txt_file(filename):
    folder = 'lab 4'
    filepath = os.path.join(folder, filename)
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"{filepath} does not exist.")
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return len(lines)
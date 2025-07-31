def count_alphabet_frequency(s):
    freq = {}
    for char in s:
        if char.isalpha():
            char_lower = char.lower()
            freq[char_lower] = freq.get(char_lower, 0) + 1
    for alphabet, count in sorted(freq.items()):
        print(f"{alphabet}: {count}")

if __name__ == "__main__":
    input_str = input("Enter a string: ")
    count_alphabet_frequency(input_str)
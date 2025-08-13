def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    input_string = input("Enter a string: ")
    return sum(1 for char in input_string if char in vowels)
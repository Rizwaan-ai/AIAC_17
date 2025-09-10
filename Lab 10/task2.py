def find_common(a, b):
    return [item for item in a if item in b]

print(find_common([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))
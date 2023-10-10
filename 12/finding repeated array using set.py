def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)

# Example Usage
arr = [1, 2, 3, 2, 1, 4, 4]
repeated_elements = find_duplicates(arr)
print(f"The repeated elements are: {repeated_elements}")

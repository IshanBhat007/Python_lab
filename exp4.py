# LINEAR
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not in the array

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 5
result = linear_search(my_list, target_value)

if result != -1:
    print(f'Target {target_value} found at index {result}.')
else:
    print(f'Target {target_value} not found in the list.')
# BINARY
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Return the index if the target is found
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if the target is not in the array

# Example usage:
my_sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 5
result = binary_search(my_sorted_list, target_value)

if result != -1:
    print(f'Target {target_value} found at index {result}.')
else:
    print(f'Target {target_value} not found in the list.')

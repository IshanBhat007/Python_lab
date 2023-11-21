def reverse_kth_row(matrix, k):
    # Check if k is a valid row index
    if k < 0 or k >= len(matrix):
        print("Invalid row index.")
        return

    # Reverse the kth row
    matrix[k] = matrix[k][::-1]

    # Print the modified matrix
    print("Matrix after reversing the", k, "th row:")
    for row in matrix:
        print(row)

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

k_value = 1  # Change this to the desired row index
reverse_kth_row(matrix, k_value)

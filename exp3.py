# Given string
my_string = "Welcome to Python World"

# Task 1: Count the number of alphabets in the string
alphabet_count = sum(c.isalpha() for c in my_string)
print(f"Number of alphabets in the string: {alphabet_count}")

# Task 2: Extract characters within a specific range from the given string
start_index = 8
end_index = 15
extracted_characters = my_string[start_index:end_index]
print(f"Characters within the range {start_index}-{end_index}: {extracted_characters}")

# Task 3: Check if the string is alphanumeric or not
is_alphanumeric = my_string.isalnum()
print(f"The string is alphanumeric: {is_alphanumeric}")

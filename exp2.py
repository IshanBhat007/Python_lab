# List example
fruits = ["apple", "banana", "orange", "grape"]

# Using a for loop to iterate over the list
print("Iterating over a list:")
for fruit in fruits:
    print(fruit)
# Dictionary example
person = {"name": "John", "age": 30, "city": "New York"}

# Using a for loop to iterate over the dictionary keys
print("\nIterating over a dictionary (keys):")
for key in person:
    print(key)

# Using a for loop to iterate over the dictionary values
print("\nIterating over a dictionary (values):")
for value in person.values():
    print(value)

# Using a for loop to iterate over both keys and values
print("\nIterating over a dictionary (keys and values):")
for key, value in person.items():
    print(f"{key}: {value}")

def demonstrate_type_checking(value):
    # Type checking
    print(f"Value: {value}")
    print(f"Type: {type(value)}")
    # Demonstrating functions
    if isinstance(value, (int, float)):
        print(f"Absolute Value: {abs(value)}")
    elif isinstance(value, str):
        print(f"Length: {len(value)}")
        print(f"Is Alphanumeric: {value.isalnum()}")
    elif isinstance(value, (list, tuple)):
        print(f"Minimum Value: {min(value)}")
    else:
        print("Unsupported data type for additional functions.")
    print("\n")
# Demonstrate with various data types
demonstrate_type_checking(42)  # Integer
demonstrate_type_checking(3.14)  # Float
demonstrate_type_checking("Hello123")  # String
demonstrate_type_checking([5, 2, 8, 1, 7])  # List
demonstrate_type_checking((10, 20, 30))  # Tuple
demonstrate_type_checking({'key': 'value'})  # Dictionary

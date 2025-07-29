
"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        # Your code here
        pass
    
    # Display original list
    print(f"Original numbers: {numbers}")
    
    # Create filtered lists
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    
    # Calculate average
    average = sum(numbers) / len(numbers)
    
    # Numbers greater than average
    above_average = [num for num in numbers if num > average]


    
    # Display results
    # Your code here

if __name__ == "__main__":
    number_operations()

def number_operations():
    numbers = []
    
    print("Enter 10 numbers:")
    for i in range(10):
        num = float(input(f"Number {i+1}: "))
        numbers.append(num)
    
    print(f"\nOriginal numbers: {numbers}")

    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    total = sum(numbers)
    average = total / len(numbers)
    min_num = min(numbers)
    max_num = max(numbers)

    above_average = [num for num in numbers if num > average]

    print(f"Even numbers: {even_numbers}")
    print(f"Odd numbers: {odd_numbers}")
    print(f"Numbers greater than average ({average:.2f}): {above_average}")

    print("\n--- Statistics ---")
    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")
    print(f"Minimum: {min_num}")
    print(f"Maximum: {max_num}")

if __name__ == "__main__":
    number_operations()

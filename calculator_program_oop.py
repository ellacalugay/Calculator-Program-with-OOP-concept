# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #7 | Calculator App with OOP concept

# Pseudocode
# Define a class named Calculator to encapsulate calculator functionality
class Calculator:
    # Create a non-parametrized constructor
    def __init__(self):
        self.operation = ""
        self.num1 = 0.0
        self.num2 = 0.0
        self.result = None

# Ask the user to choose one of the four math operations 
    def get_operation(self):
        self.operation = str(input("Please choose among the four operations - Addition, Subtraction, Multiplication, Division: "))
        
# Ask the user for two numbers
    def get_two_numbers(self):
        print("Kindly input two numbers.")
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))
        
# Perform the calculation based on the operation that the user wants
# Display the result
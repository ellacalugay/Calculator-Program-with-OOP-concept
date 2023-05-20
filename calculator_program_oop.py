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
    def perform_operation(self):
        if self.operation == "Addition":
            # If the operation is Addition, add the two numbers.
            self.result = self.num1 + self.num2
        elif self.operation == "Subtraction":
            # If the operation is Subtraction, subtract the second number from the first number
            self.result = self.num1 - self.num2
        elif self.operation == "Multiplication":
            # If the operation is Multiplication, multiply the two numbers.
            self.result = self.num1 * self.num2
        elif self.operation == "Division":
            # If the operation is Division, divide the first number by the second number.
            self.result = self.num1 / self.num2
        else:
            raise ValueError("Invalid Operation")
    
# Display the result
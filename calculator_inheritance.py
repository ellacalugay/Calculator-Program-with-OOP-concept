# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #8 | Calculator App with OOP concept and inheritance

# Pseudocode
# Create an inheritance from calculator.py
# Importing the Calculator class from calculator_program_oop module
from calculator_program_oop import Calculator

# Defining the ScientificCalculator class that inherits from the Calculator class
class ScientificCalculator(Calculator):
    # Create a non-parametrized constructor
    def __init__(self):
        # Calling the constructor of the parent class
        super().__init__()
        
    # Computation for the square root
    def compute_square_root(self):
        try:
            self.get_two_numbers() # Calling the get_two_numbers method from the parent class to get input from the user
            self.result = self.num1 + self.num2
        except ValueError:
            self.result = None
            ("Error", "Invalid input. Please enter valid numbers.")
        except Exception as err:
            self.result = None
            ("Error", f"An error occurred: {str(err)}")
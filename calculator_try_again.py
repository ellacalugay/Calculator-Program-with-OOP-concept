# Pseudocode
# Import the Calculator class from the calculator_program_oop module
from calculator_program_oop import Calculator

# Define a class named Retry
class Retry:
# Create a non-parametrized constructor
    def __init__(self):
        self.retry = ""

# Ask if the user wants to try again or not.
    def ask_retry(self):
        while True:
            try_again = input("Do you want to try again? (yes/no): ")
            
# If yes, repeat the process.
# If no, Display “Thank you!” and exit the program.
# Exit the loop
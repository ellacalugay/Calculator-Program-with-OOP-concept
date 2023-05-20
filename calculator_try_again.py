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
            if try_again.lower() == "yes":
                calculator = Calculator()
                calculator.get_operation()
                calculator.get_two_numbers()
                calculator.perform_operation()
                calculator.display_result()
            # If no, Display “Thank you!” and exit the program.
            elif try_again.lower() == "no":
                print("Thank you.")
                break # Exit the loop
            else: 
                print("Invalid input. Please enter 'yes' or 'no'.")
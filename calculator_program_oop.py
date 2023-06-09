# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #7 | Calculator App with OOP concept

# Pseudocode
# ASCII art for the header with ANSI escape codes for color
print(("\033[38;5;218m" + """
 _____________________
|  _________________  |
| |  Simple      0. | |
| |     Calculator  | |
| |           App   | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""+ "\033[0m"))

# Import the necessary modules
from tkinter import messagebox

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
        while True:
            try: 
                self.num1 = float(input("Enter the first number: "))
                self.num2 = float(input("Enter the second number: "))
                break  # Break the loop if valid input is provided
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
# Perform the calculation based on the operation that the user wants
    def perform_operation(self):
        try:
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
                if self.num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero. Please enter a non-zero value for the second number.")
                self.result = self.num1 / self.num2
            else:
                self.result = None
                messagebox.showerror("Error", "Invalid operation selected")
        # Appropriate Exceptions to capture errors during runtime.
        except ZeroDivisionError as e:
            self.result = None
            messagebox.showerror("Error", str(e))
        except Exception as err:
            self.result = None
            messagebox.showerror("Error", f"An error occurred: {str(err)}")
        
# Display the result
    def display_result(self):
        if self.result is not None:
            messagebox.showinfo("Result", f"The result is: {self.result}")
        else:
            messagebox.showerror("Error", "Operation failed.")

# End of the code
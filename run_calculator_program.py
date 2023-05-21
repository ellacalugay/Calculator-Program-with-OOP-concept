# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #7 | Calculator App with OOP concept

# Import the necessary modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Import the Calculator class from the calculator_program_oop module
from calculator_program_oop import Calculator
# Import the Retry class from the calculator_try_again module
from calculator_try_again import Retry

# Define a class named CalculatorApp for the tkinter window design
class CalculatorApp:
    # Create a non-parametrized constructor
    def __init__(self):
        # Create instances of the Calculator and Retry
        self.calculator = Calculator()
        self.retry = Retry()

        # Ask the user for the desired operation
        self.calculator.get_operation()

        # Ask the user to input two numbers
        self.calculator.get_two_numbers()

        # Perform the operation based on the user's input
        self.calculator.perform_operation()

        # Display the result
        self.calculator.display_result()

        # Ask if the user wants to try again
        self.retry.ask_retry()
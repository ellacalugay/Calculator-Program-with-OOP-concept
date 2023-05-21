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

    # Create instances of the Calculator and Retry
    selcalculator = Calculator()
    retry = Retry()

    # Ask the user for the desired operation
    calculator.get_operation()

    # Ask the user to input two numbers
    calculator.get_two_numbers()

    # Perform the operation based on the user's input
    calculator.perform_operation()

    # Display the result
    calculator.display_result()

    # Ask if the user wants to try again
    retry.ask_retry()
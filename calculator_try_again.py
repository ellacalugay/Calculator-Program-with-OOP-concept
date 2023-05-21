# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #7 | Calculator App with OOP concept

# Pseudocode
# Import the necessary modules
from tkinter import messagebox

# Define a class named Retry
class Retry:
# Create a non-parametrized constructor
    def __init__(self):
        self.retry = ""

# Ask if the user wants to try again or not.
    def ask_retry(self):
        while True:
            try_again = messagebox.askquestion("Retry", "Do you want to try again?")
            # If yes, repeat the process.
            if try_again == "yes":
                return True
            # If no, Display “Thank you!” and exit the program.
            elif try_again == "no":
                return False
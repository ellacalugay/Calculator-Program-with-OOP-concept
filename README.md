# SIMPLE CALCULATOR with OOP concept and INHERITANCE
This program has 4 python files each one have a class.
-----------------------------------------------------------
# Calculator class: 
This class encapsulates the basic calculator functionality. It has methods to get the desired operation from the user, get two numbers for calculation, perform the operation, and display the result.

# ScientificCalculator class: 
This class inherits from the Calculator class and adds a method to compute the square root of a number. It overrides the display_result method to display the square root in addition to the result.

# Retry class: 
This class provides functionality to ask the user if they want to try again or exit the program.

# CalculatorApp class: 
This class represents the graphical user interface (GUI) of the calculator application using the tkinter library. It creates an instance of the ScientificCalculator and Retry classes. It sets up the UI widgets for the calculator app, binds events, and handles user input. It also includes methods to calculate the result, clear the input fields, and run the application.

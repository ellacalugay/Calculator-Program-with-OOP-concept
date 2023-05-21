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

        # Initialize tkinter app
        self.root = tk.Tk()
        self.root.title("Simple Calculator")
        self.root.configure(background='pink')

        # Set style
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12))

        # Create and set up the UI widgets for the calculator app
        self.create_widgets()
        # Bind the <Return> key event to the calculate method
        self.bind_events() 

    # Create widgets for the design
    def create_widgets(self):
        # Create a label widget for the header of the calculator app
        self.label_header = tk.Label(self.root, text="Simple Calculator App", font=('Helvetica', 16, 'bold'), bg='light blue')
        self.label_header.pack(pady=10)

        # Create a frame widget to hold the input elements
        self.frame_input = ttk.Frame(self.root)
        self.frame_input.pack(pady=15)

        # Create a frame widget to hold the input elements
        self.label_operation = ttk.Label(self.frame_input, text="Choose an operation:", foreground="black", background="light coral", font=(20))
        self.label_operation.grid(row=0, column=0, padx=5)

        # Create a combobox widget for selecting the operation
        self.combo_operation = ttk.Combobox(self.frame_input, values=["Addition", "Subtraction", "Multiplication", "Division"])
        self.combo_operation.grid(row=0, column=1, padx=5)

        # Create label and entry widgets for the first number input
        self.label_num1 = ttk.Label(self.frame_input, text="First number:", foreground='gold', background="maroon")
        self.label_num1.grid(row=1, column=0, padx=5)
        self.entry_num1 = ttk.Entry(self.frame_input)
        self.entry_num1.grid(row=1, column=1, padx=5)

        # Create label and entry widgets for the second number input
        self.label_num2 = ttk.Label(self.frame_input, text="Second number:", foreground='gold', background="maroon")
        self.label_num2.grid(row=2, column=0, padx=5)
        self.entry_num2 = ttk.Entry(self.frame_input)
        self.entry_num2.grid(row=2, column=1, padx=5)

        # Create a frame widget to hold the buttons
        self.frame_buttons = ttk.Frame(self.root)
        self.frame_buttons.pack(pady=10)

        # Create a button widget for calculating the result, with a command to execute when clicked
        self.button_calculate = tk.Button(self.frame_buttons, text="Calculate", bg='yellow', command=self.calculate)
        self.button_calculate.pack(side=tk.LEFT, padx=5)

        # Create a button widget for clearing the input fields, with a command to execute when clicked
        self.button_clear = tk.Button(self.frame_buttons, text="Clear", bg="red", command=self.clear)
        self.button_clear.pack(side=tk.LEFT, padx=5)

    # Bind the <Return> key event to the calculate method
    def bind_events(self):
        self.root.bind("<Return>", self.calculate) 

    def calculate(self, event=None):
        try:
        # Ask the user for the desired operation
            self.calculator.operation = str(self.combo_operation.get())
            # Ask the user to input two numbers
            self.calculator.num1 = float(self.entry_num1.get())
            self.calculator.num2 = float(self.entry_num2.get())
        except ValueError:
            # Handle any errors that occur during the calculation
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
            return
        
        # Perform the operation based on the user's input
        self.calculator.perform_operation()

        # Display the result
        self.calculator.display_result()

        # Ask if the user wants to try again
        if self.retry.ask_retry():
            self.clear()
        else:
            # Display "Thank you" message
            messagebox.showinfo("Exit", "Thank you for using our program!")
            # Close the application
            self.root.destroy()
        
    def clear(self):
        self.combo_operation.set("") # Clear the selected operation in the combobox
        self.entry_num1.delete(0, tk.END) # Clear the first number entry field
        self.entry_num2.delete(0, tk.END) # Clear the second number entry field

    def run(self):
        # Start the main event loop to run the application
        self.root.mainloop()

# Create an instance of CalculatorApp and run the app
app = CalculatorApp()
app.run()

# End of the code.
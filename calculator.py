import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("380x560")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")

        self.expression = ""

        # -------------------------
        # Display
        # -------------------------
        self.display = tk.Entry(
            root,
            font=("Arial", 28),
            bg="#252526",
            fg="white",
            insertbackground="white",
            justify="right",
            bd=0,
            relief="flat"
        )

        self.display.pack(
            padx=15,
            pady=(20, 10),
            fill="both",
            ipady=20
        )

        # -------------------------
        # Button Frame
        # -------------------------
        button_frame = tk.Frame(
            root,
            bg="#1e1e1e"
        )

        button_frame.pack(
            padx=10,
            pady=10,
            fill="both",
            expand=True
        )

        # Button layout
        buttons = [
            ["C", "⌫", "(", ")"],
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "−"],
            ["0", ".", "%", "+"],
            ["="]
        ]

        # Configure rows
        for row in range(6):
            button_frame.rowconfigure(row, weight=1)

        # Configure columns
        for col in range(4):
            button_frame.columnconfigure(col, weight=1)

        # -------------------------
        # Create Buttons
        # -------------------------
        for row_index, row in enumerate(buttons):

            for col_index, button_text in enumerate(row):

                # "=" button takes full width
                if button_text == "=":
                    button = tk.Button(
                        button_frame,
                        text=button_text,
                        font=("Arial", 20, "bold"),
                        bg="#0078D4",
                        fg="white",
                        activebackground="#005A9E",
                        activeforeground="white",
                        bd=0,
                        command=self.calculate
                    )

                    button.grid(
                        row=row_index,
                        column=0,
                        columnspan=4,
                        sticky="nsew",
                        padx=5,
                        pady=5
                    )

                else:
                    # Different colors for special buttons
                    if button_text in ["+", "−", "×", "÷"]:
                        bg_color = "#FF9500"
                        active_color = "#CC7700"

                    elif button_text in ["C", "⌫", "(", ")", "%"]:
                        bg_color = "#3A3A3A"
                        active_color = "#505050"

                    else:
                        bg_color = "#2D2D2D"
                        active_color = "#404040"

                    button = tk.Button(
                        button_frame,
                        text=button_text,
                        font=("Arial", 18, "bold"),
                        bg=bg_color,
                        fg="white",
                        activebackground=active_color,
                        activeforeground="white",
                        bd=0,
                        command=lambda value=button_text: self.button_click(value)
                    )

                    button.grid(
                        row=row_index,
                        column=col_index,
                        sticky="nsew",
                        padx=5,
                        pady=5
                    )

        # Keyboard support
        self.root.bind("<Key>", self.keyboard_input)
        self.display.focus_set()

    # -------------------------
    # Button Click Handler
    # -------------------------
    def button_click(self, value):

        if value == "C":
            self.clear()

        elif value == "⌫":
            self.backspace()

        else:
            self.expression += value
            self.update_display()

    # -------------------------
    # Update Display
    # -------------------------
    def update_display(self):

        display_expression = self.expression

        # Make mathematical symbols user-friendly
        display_expression = display_expression.replace("*", "×")
        display_expression = display_expression.replace("/", "÷")

        self.display.delete(0, tk.END)
        self.display.insert(0, display_expression)

    # -------------------------
    # Clear
    # -------------------------
    def clear(self):

        self.expression = ""

        self.display.delete(0, tk.END)

    # -------------------------
    # Backspace
    # -------------------------
    def backspace(self):

        if self.expression:
            self.expression = self.expression[:-1]
            self.update_display()

    # -------------------------
    # Calculate
    # -------------------------
    def calculate(self):

        if not self.expression:
            return

        try:
            # Convert calculator symbols to Python operators
            expression = self.expression

            expression = expression.replace("×", "*")
            expression = expression.replace("÷", "/")
            expression = expression.replace("−", "-")

            # Handle percentage
            expression = self.convert_percentage(expression)

            # Evaluate expression
            result = eval(
                expression,
                {
                    "__builtins__": None
                },
                {}
            )

            # Avoid displaying 5.0 instead of 5
            if isinstance(result, float) and result.is_integer():
                result = int(result)

            self.expression = str(result)

            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))

        except ZeroDivisionError:
            self.show_error("Cannot divide by zero.")

        except (SyntaxError, TypeError, ValueError):
            self.show_error("Invalid expression.")

        except Exception:
            self.show_error("Something went wrong.")

    # -------------------------
    # Percentage Handler
    # -------------------------
    def convert_percentage(self, expression):

        result = ""
        number = ""

        for char in expression:

            if char.isdigit() or char == ".":
                number += char

            else:

                if number:
                    result += str(float(number) / 100)
                    number = ""

                result += char

        if number:
            result += str(float(number) / 100)

        return result

    # -------------------------
    # Error Message
    # -------------------------
    def show_error(self, message):

        messagebox.showerror(
            "Calculator Error",
            message
        )

        self.clear()

    # -------------------------
    # Keyboard Input
    # -------------------------
    def keyboard_input(self, event):

        key = event.keysym
        char = event.char

        # Numbers
        if char.isdigit():
            self.expression += char
            self.update_display()

        # Decimal
        elif char == ".":
            self.expression += "."
            self.update_display()

        # Operators
        elif char in "+-*/":
            operator = char

            if operator == "*":
                operator = "×"

            elif operator == "/":
                operator = "÷"

            elif operator == "-":
                operator = "−"

            self.expression += operator
            self.update_display()

        # Parentheses
        elif char in "()":
            self.expression += char
            self.update_display()

        # Percentage
        elif char == "%":
            self.expression += "%"
            self.update_display()

        # Enter / Return
        elif key in ("Return", "KP_Enter"):
            self.calculate()

        # Backspace
        elif key == "BackSpace":
            self.backspace()

        # Escape
        elif key == "Escape":
            self.clear()


# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":

    root = tk.Tk()

    calculator = Calculator(root)

    root.mainloop()
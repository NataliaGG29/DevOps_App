import tkinter as tk

# Update input
def click_button(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Evaluate the result
def evaluate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except Exception:
        input_text.set("Error")
        expression = ""

# clean the input
def clear():
    global expression
    expression = ""
    input_text.set("")

# Set up the principal window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")

expression = ""
input_text = tk.StringVar()

# input
input_frame = tk.Frame(window)
input_frame.pack(pady=10)
input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), width=50, bd=5, insertwidth=4, justify='right')
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Buttons
button_frame = tk.Frame(window)
button_frame.pack()

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(button_frame, text=text, font=('arial', 18, 'bold'), fg='black', width=10, height=3, bd=1,
                       command=lambda t=text: click_button(t) if t != '=' else evaluate())
    button.grid(row=row, column=col, padx=1, pady=1)

clear_button = tk.Button(button_frame, text='C', font=('arial', 18, 'bold'), fg='black', width=10, height=3, bd=1, command=clear)
clear_button.grid(row=4, column=0, padx=1, pady=1)

window.mainloop()


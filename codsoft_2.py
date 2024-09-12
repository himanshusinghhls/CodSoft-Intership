import tkinter as tk

def calculate():
    try:
        n1 = int(num1_entry.get())
        n2 = int(num2_entry.get())
        opt = operator_entry.get()

        if opt == '+':
            result = n1 + n2
        elif opt == '-':
            result = n1 - n2
        elif opt == '*':
            result = n1 * n2
        elif opt == '/':
            if n2 != 0:
                result = n1 / n2
            else:
                result_label.config(text="Error: Division by zero!")
                return
        else:
            result_label.config(text="Error: Invalid operator!")
            return

        result_label.config(text=f"{n1} {opt} {n2} = {result}")
    except ValueError:
        result_label.config(text="Error: Invalid input!")

root = tk.Tk()
root.title("Simple Calculator")

num1_label = tk.Label(root, text="Number 1:")
num1_label.pack()
num1_entry = tk.Entry(root)
num1_entry.pack()

num2_label = tk.Label(root, text="Number 2:")
num2_label.pack()
num2_entry = tk.Entry(root)
num2_entry.pack()

operator_label = tk.Label(root, text="Operator {+,-,*,/}:")
operator_label.pack()
operator_entry = tk.Entry(root)
operator_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

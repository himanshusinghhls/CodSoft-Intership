import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 8:
            result_label.config(text="Error: Password length must be at least 8 characters.")
            return
        ch = string.ascii_letters + string.digits + "@" + "#" + "&" + "_"
        password = ''.join(random.choice(ch) for i in range(length))
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        result_label.config(text="Error: Invalid input!")

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter the length of the password:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

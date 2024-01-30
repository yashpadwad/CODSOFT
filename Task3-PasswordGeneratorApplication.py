
import tkinter as tk
import string
import random
def generate_password():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    plen = length_var.get()
    password = "".join(random.sample(s, plen))
    password_display.config(text="Your password is: " + password, fg="green")
root = tk.Tk()
root.title("Password Generator")
frame = tk.Frame(root)
frame.pack(pady=10)
label = tk.Label(frame, text="Enter password length:", fg="blue")
label.pack()
length_var = tk.IntVar()
entry = tk.Entry(frame, width=50, textvariable=length_var)
entry.pack()
generate_button = tk.Button(root, text="Generate Password", width=48, command=generate_password, bg="yellow")
generate_button.pack()
password_display = tk.Label(root, text="", fg="green")
password_display.pack()
root.mainloop()
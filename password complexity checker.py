import tkinter as tk
from tkinter import ttk
import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None

    strength = 0
    if length_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if number_criteria:
        strength += 1
    if special_criteria:
        strength += 1

    return strength, length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria

def check_password():
    password = password_entry.get()
    strength, length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria = assess_password_strength(password)

    feedback = "Password strength assessment:\n"
    feedback += f"Length >= 8: {'✔️' if length_criteria else '❌'}\n"
    feedback += f"Contains uppercase: {'✔️' if uppercase_criteria else '❌'}\n"
    feedback += f"Contains lowercase: {'✔️' if lowercase_criteria else '❌'}\n"
    feedback += f"Contains number: {'✔️' if number_criteria else '❌'}\n"
    feedback += f"Contains special character: {'✔️' if special_criteria else '❌'}\n"

    if strength == 5:
        feedback += "\nPassword Strength: Very Strong"
    elif strength >= 3:
        feedback += "\nPassword Strength: Strong"
    elif strength == 2:
        feedback += "\nPassword Strength: Medium"
    else:
        feedback += "\nPassword Strength: Weak"

    feedback_label.config(text=feedback)

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")

# Instructions label
instructions = ttk.Label(root, text="Enter a password to assess its strength:")
instructions.grid(column=0, row=0, padx=10, pady=10)

# Password entry
password_entry = ttk.Entry(root, show='*')
password_entry.grid(column=0, row=1, padx=10, pady=10)

# Check button
check_button = ttk.Button(root, text="Check Password Strength", command=check_password)
check_button.grid(column=0, row=2, padx=10, pady=10)

# Feedback label
feedback_label = ttk.Label(root, text="")
feedback_label.grid(column=0, row=3, padx=10, pady=10)

# Start the main loop
root.mainloop()

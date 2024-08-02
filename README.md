# PRODIGY_CS_03
# Password Strength Checker

This is a Python tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. The tool provides feedback to users on the password's strength through a graphical user interface (GUI) built using Tkinter.

## Features

- *Length Check*: Ensures the password is at least 8 characters long.
- *Uppercase Check*: Checks for the presence of uppercase letters.
- *Lowercase Check*: Checks for the presence of lowercase letters.
- *Number Check*: Checks for the presence of numbers.
- *Special Character Check*: Checks for the presence of special characters.
- *Feedback*: Provides real-time feedback on the strength of the password.

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter (usually included with Python)

### Installation

1. *Clone the repository*:

   git clone https://github.com/Anasmc24/PRODIGY_CS_03/tree/main
   cd password-strength-checker

2.*Ensure Tkinter is installed*:
For Debian-based systems (e.g., Ubuntu):
sudo apt-get install python3-tk

For Windows, Tkinter is included with Python. If needed, you can install it using:
pip install tk

Running the Application

*Navigate to the project directory*:
cd password-strength-checker

*Run the application*:
python password_strength_checker.py

*Usage*
Enter a Password: Type a password into the input field.
Check Password Strength: Click the "Check Password Strength" button.
View Feedback: The feedback label will display the assessment of the password based on the criteria.

*Example*
Input Password: P@ssw0rd
Feedback:
yaml
Copy code
Password strength assessment:
Length >= 8: ✔️
Contains uppercase: ✔️
Contains lowercase: ✔️
Contains number: ✔️
Contains special character: ✔️

Password Strength: Very Strong

# Password Generator 🛠️

This is a simple yet efficient password generator application built using Python's tkinter library. The app allows users to generate strong, random passwords, save them with associated website and email information, and store this data for future reference. The program also provides an option to copy the generated password to the clipboard for easy use.

## Features ✨

Random Password Generation 🔑: Generates a secure password containing a mix of letters, numbers, and symbols.
Password Storage 💾: Users can save passwords along with website URLs and email/username information in a file for easy retrieval.
Clipboard Copy 📋: The generated password is automatically copied to the clipboard for quick use.
User-Friendly Interface 💻: Built using tkinter, offering a clean and simple interface for managing passwords.

## Requirements 📝

Python 3.x 🐍
pyperclip (for clipboard functionality) 📥


## Usage 💡

Generate a Password: Enter the website name and email (optional), then click the "Generate" button. A random password will be generated and copied to your clipboard.
Save Password: Enter the website and email (optional), and click the "Add" button to save the website, email, and generated password into a passwords.txt file.
The passwords are saved in the following format:

## Code Overview 🛠️

Main Features and Functions:
Password Generation: The password_aleatoria function creates a random password with a mix of letters, numbers, and symbols. The length of the password is randomly determined between 8 and 10 characters, with additional random characters from the letters, numbers, and symbols lists.

Password Saving: The save function ensures that both the website and password fields are filled before allowing the user to save the information. If confirmed, the data is appended to a passwords.txt file for storage.

Graphical User Interface: The GUI is created using the tkinter library. Labels, entry fields, and buttons are arranged to allow for easy interaction. A custom logo is included for branding purposes.

## Key Components:
Labels: Created using a custom class (Labels), the labels are used for displaying text next to input fields (e.g., "Website:", "Email/Username:", "Password:").
Input Fields: Custom input fields are created using the Entradas class. These fields allow users to enter the website, email, and password.
Buttons: Buttons are created using the Botones class, which triggers the password generation and saving actions.
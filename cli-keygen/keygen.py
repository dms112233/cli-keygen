'''Copyright (C) <2025> <Evrotskii Artem>
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at your option)
any later version.
'''

from random import randint
import string
import tkinter as tk
from tkinter import ttk

class Keygen:
    def __init__(self, lenght:int=-1):
        self._lenght = lenght
        self.all_chars = string.ascii_letters + string.digits + string.punctuation
        self.password = ""

    def generate(self, lenght:int):
        self.password = ""  # Reset password before generating new one
        if self._lenght == -1:
            self._lenght = lenght

        for _ in range(self._lenght):
            self.password += self.all_chars[randint(0, len(self.all_chars) - 1)]
        return self.password

class PasswordGeneratorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Generator")
        self.window.geometry("400x200")
        self.keygen = Keygen()
        
        # Create and pack widgets
        self.length_label = ttk.Label(self.window, text="Password Length:")
        self.length_label.pack(pady=10)
        
        self.length_entry = ttk.Entry(self.window)
        self.length_entry.pack(pady=5)
        self.length_entry.insert(0, "12")
        
        self.generate_button = ttk.Button(self.window, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)
        
        self.password_var = tk.StringVar()
        self.password_label = ttk.Label(self.window, textvariable=self.password_var)
        self.password_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            password = self.keygen.generate(length)
            self.password_var.set(password)
        except ValueError:
            self.password_var.set("Please enter a valid number")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = PasswordGeneratorGUI()
    app.run()

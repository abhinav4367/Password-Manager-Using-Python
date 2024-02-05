import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
import random
import string

class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")

        # Create database and table
        self.conn = sqlite3.connect('passwords.db')
        self.cursor = self.conn.cursor()
        self.create_table()  # Call create_table to initialize or reset the database table

        # Widgets
        self.label_website = tk.Label(master, text="Website:")
        self.label_username = tk.Label(master, text="Username:")
        self.label_password = tk.Label(master, text="Password:")

        self.entry_website = tk.Entry(master)
        self.entry_username = tk.Entry(master)
        self.entry_password = tk.Entry(master, show='*')  # Passwords are initially shown as asterisks

        self.btn_generate_password = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.btn_add_password = tk.Button(master, text="Add Password", command=self.add_password)
        self.btn_show_passwords = tk.Button(master, text="Show Passwords", command=self.show_passwords)
        self.btn_remove_password = tk.Button(master, text="Remove Password", command=self.remove_password)
        self.btn_reset_database = tk.Button(master, text="Reset Database", command=self.reset_database)

        # Layout
        self.label_website.grid(row=0, column=0, padx=10, pady=10)
        self.label_username.grid(row=1, column=0, padx=10, pady=10)
        self.label_password.grid(row=2, column=0, padx=10, pady=10)

        self.entry_website.grid(row=0, column=1, padx=10, pady=10)
        self.entry_username.grid(row=1, column=1, padx=10, pady=10)
        self.entry_password.grid(row=2, column=1, padx=10, pady=10)

        self.btn_generate_password.grid(row=2, column=2, padx=10, pady=10)
        self.btn_add_password.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.btn_show_passwords.grid(row=4, column=0, padx=10, pady=10)
        self.btn_remove_password.grid(row=4, column=1, padx=10, pady=10)
        self.btn_reset_database.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def create_table(self):
        # Create or reset the database table
        self.cursor.execute('''
            DROP TABLE IF EXISTS passwords
        ''')
        self.cursor.execute('''
            CREATE TABLE passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                website TEXT,
                username TEXT,
                password TEXT
            )
        ''')
        self.conn.commit()

    def generate_password(self):
        # Generate a random password
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
        self.entry_password.delete(0, tk.END)
        self.entry_password.insert(0, password)

    def add_password(self):
        # Add the password details to the database
        website = self.entry_website.get()
        username = self.entry_username.get()
        password = self.entry_password.get()

        if website and username and password:
            self.cursor.execute('''
                INSERT INTO passwords (website, username, password)
                VALUES (?, ?, ?)
            ''', (website, username, password))
            self.conn.commit()
            messagebox.showinfo("Success", "Password added successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def show_passwords(self):
        # Prompt for a key before revealing passwords
        key = simpledialog.askstring("Key", "Enter the key to reveal passwords:", show='*')
        if key == "admin":  # Change "your_secret_key" to your actual secret key
            # Display all stored passwords
            passwords = self.cursor.execute("SELECT * FROM passwords").fetchall()
            if passwords:
                result_text = "\n".join([f"Website: {row[1]}\nUsername: {row[2]}\nPassword: {row[3]}\n" for row in passwords])
                messagebox.showinfo("Stored Passwords", result_text)
            else:
                messagebox.showinfo("Stored Passwords", "No passwords stored yet.")
        else:
            messagebox.showinfo("Access Denied", "Incorrect key. Passwords not revealed.")

    def remove_password(self):
        # Prompt for a key before removing passwords
        key = simpledialog.askstring("Key", "Enter the key to remove passwords:", show='*')
        if key == "admin":  # Change "your_secret_key" to your actual secret key
            website = self.entry_website.get()
            username = self.entry_username.get()

            if website and username:
                self.cursor.execute('''
                    DELETE FROM passwords
                    WHERE website=? AND username=?
                ''', (website, username))
                self.conn.commit()
                messagebox.showinfo("Success", "Password removed successfully!")
            else:
                messagebox.showerror("Error", "Please fill in website and username fields.")
        else:
            messagebox.showinfo("Access Denied", "Incorrect key. Passwords not removed.")

    def reset_database(self):
        # Prompt for a key before resetting the database
        key = simpledialog.askstring("Key", "Enter the key to reset the database:", show='*')
        if key == "admin":  # Change "your_secret_key" to your actual secret key
            self.create_table()
            messagebox.showinfo("Success", "Database reset successfully!")
        else:
            messagebox.showinfo("Access Denied", "Incorrect key. Database not reset.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()

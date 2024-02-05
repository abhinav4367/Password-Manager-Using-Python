# Password-Manager-Using-Python
> This simple Password Manager application is built using Tkinter and SQLite for managing and storing passwords securely. It provides basic functionalities to generate, add, display, and remove passwords.

## Features
- **Generate Password**: Automatically generates a random password consisting of letters, digits, and punctuation.
- **Add Password**: Stores website, username, and password information securely in the database.
- **Show Passwords**: Displays stored passwords after verifying a key for added security.
- **Remove Password**: Removes stored passwords after verifying a key for added security.
- **Reset Database**: Clears all stored passwords and resets the database after verifying a key.

## Dependencies
- **Python 3.x**
- **Tkinter** (usually included with Python installations)
- **SQLite** (usually included with Python installations)

## Usage
Follow these steps to set up and use the Password Manager
### **Step 1: Clone the Repository**
```bash
git clone https://github.com/abhinav4367/Password-Manager-Using-Python.git
cd [Password-Manager-Using-Python]
```
### **Step 2: Run the Password Manager**
```
python [filename].py
```
### **Step 3: Interface Overview**
The Password Manager interface consists of the following components:

- **Website**: Entry for the website or service name.
- **Username**: Entry for the username associated with the website.
- **Password**: Entry for the password; click "Generate Password" to create a random password.
- **Generate Password**: Button to generate a random password.
- **Add Password**: Button to add the current details to the password database.
- **Show Passwords**: Button to display stored passwords (requires a key).
- **Remove Password**: Button to delete a stored password (requires a key).
- **Reset Database**: Button to clear all stored passwords (requires a key).
### **Step 4: Generate and Add Passwords**
- Fill in the Website, Username, and Password fields.
- Optionally, click Generate Password for an automatically generated password.
- Click Add Password to store the credentials in the database.
### **Step 5: Show Stored Passwords**
- Click Show Passwords.
- Enter the correct key (default: "admin") to reveal stored passwords.
- View and take note of the displayed passwords.
### **Step 6: Remove Stored Password**
- Fill in the Website and Username fields.
- Click Remove Password.
- Enter the correct key to delete the associated password.
### **Step 7: Reset the Database**
- Click Reset Database.
- Enter the correct key to clear all stored passwords.
Note: Always keep your key secure and do not share it with unauthorized individuals.

### Database
The application uses an SQLite database named passwords.db with a table named passwords. The table schema includes columns for id (auto-incrementing primary key), website, username, and password.

### Security
The application prompts for a key (password) before allowing access to sensitive operations like displaying, removing, or resetting passwords. This adds an extra layer of security to protect stored password information.

Note: It is recommended to customize the access key by modifying the key variable in the show_passwords, remove_password, and reset_database methods.

### Warning
Please use this application responsibly and keep your access key secure. The application is a simple example and may not provide advanced security features found in professional password management solutions.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to modify and enhance the application according to your needs. Happy coding!


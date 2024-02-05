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
Follow these steps to set up and use the Password Manager:
1.Step 1: Clone the Repository

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


# Imports
import random, sys, os, platform
from colorama import init, Fore, Style

init() # Initialize colorama

# Create password function
def create_password() -> str:
    lower: str = 'abcdefghijklmnopqrstuvwxyz' # Lower caracteres
    upper: str = lower.upper() # Upper caracteres

    numbers: str = '0123456789' # Numbers
    symbols: str = '!@#$%&*;.,_' # Symbols

    all_caracters: str = lower + upper + numbers + symbols # Add all caracteres in one string
    length: int = 18 # Set the password length

    return ''.join(random.sample(all_caracters, length)) # Creates the password and returns it

# Write password file function
def write_password_file(new_password: str) -> list:
    lines: list = [] # Lines of the file

    if os.path.exists('./py-passwords.txt'): # If the file already exists, then...
        file = open('py-passwords.txt', 'r') # Open file in READ mode

        for line in file:
            lines.append(f'{line.rstrip()}\n') # Append the old password to the list


    lines.append(new_password) # Append the new password to the list

    file = open('py-passwords.txt', 'w') # Open file in WRITE mode
    file.writelines(lines) # Write the passwords in the file
    file.close() # Close file editing

    return lines # Return the password in the file

done: bool = False # Loop variable
passwords: list = [] # File passwords
os_platform = platform.system() # Current OS platform

# Main loop
while not done:

    print('--------------------------------')
    print(Fore.LIGHTGREEN_EX + '     - Password Generator -     ' + Style.RESET_ALL)
    print('--------------------------------')
    print('')

    action: str = input(' - Want to create a new password? (Y/n) ') # Ask to the user if he wants to create a new password
    print('')

    if action == 'Y' or action == 'y': # If the user wants to create a new password, then...
        password_name: str = input(' - Provide a name for your password: ') # Gets the password name
        created_password: str = create_password() # Creates a new password

        passwords = write_password_file(f'{password_name}: {created_password}') # Write the created password in the file
    else:
        done = True # Else, stop the loop

    if os_platform == 'Windows':
        os.system('cls') # Runs CLS command if is windows
    else:
        os.system('clear') # Else, runs CLEAR command if is MAC or Linux

# If any password exists in the passwords list, then...
if len(passwords) > 0:
    print('')
    print(Fore.LIGHTGREEN_EX + '------------ Generated Passwords ------------' + Style.RESET_ALL)
    print('')

    for password in passwords:
        print(f' - {password}') # Print the passwords

sys.exit() # Exit script

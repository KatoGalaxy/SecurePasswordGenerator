# Lab 1: Secure Password Generator
# Name: Kato Burns
# Date: January 24, 2025
# Generates a password, length determined by user. User can also force a certain number of characters in the password to be a specific type.


# libraries
import string
import random

# Gets an int (or could also be used for float?) from the user. Returns it if it's within a specified range, or asks again if it isn't
def get_user_input(prompt, min_value, max_value):
    input_loop = True
    while input_loop == True:
        try:
            user_input = int(input(prompt))
            if user_input >= min_value and user_input <= max_value:
                input_loop = False
                return user_input
            else:
                print("ERROR - Input is not within the valid range.")
        except:
            print("ERROR - Input must be a number.")

# Generates a random password of a certain length. Number of letters, digits, and special chars is specfifed.
# If the entire length isn't used it will fill the remaining slots with random characters of any type
def generate_password(length, num_letters, num_digits, num_specials):
    password = []
    password_string = ""
    empty_characters = length - num_letters - num_digits - num_specials

    for x in range(num_letters):
        password.append(random.choice(string.ascii_letters))

    for x in range(num_digits):
        password.append(random.choice(string.digits))

    for x in range(num_specials):
        password.append(random.choice(string.punctuation))

    for x in range(empty_characters):
        password.append(random.choice(string.printable))

    random.shuffle(password)

    for x in password:
        password_string += x + ''
    
    return password_string


# Main function
# This is where the actual program runs. Sets varibles and calls functions, also prints the completed password
def main():
    print("\n--- Secure Password Generator ---\n")
    
    # variables
    password_length = 0
    password_length_remaining = 0
    letter_count = 0
    digit_count = 0
    sp_char_count = 0
    
    # The main process. Gets the input for each step, and updates the variables above. Finally generates a password based on the variables
    password_length = get_user_input("Please enter the desired password length (min 8 char - max 128): ", 8, 128)
    password_length_remaining = password_length
    letter_count = get_user_input("Please enter the number of letters in the password (" + str(password_length_remaining) + " characters remaining): ", 0, password_length_remaining)
    password_length_remaining -= letter_count
    digit_count = get_user_input("Please enter the number of digits in the password (" + str(password_length_remaining) + " characters remaining): ", 0, password_length_remaining)
    password_length_remaining -= digit_count
    sp_char_count = get_user_input("Please enter the number of SP characters in the password (" + str(password_length_remaining) + " characters remaining): ", 0, password_length_remaining)
    password_length_remaining -= sp_char_count
    password = generate_password(password_length, letter_count, digit_count, sp_char_count)

    # Prints the generated password.
    print("Generated password: " + password)

    # Writes the password to a file named "password.txt"
    f = open("password.txt", "w")
    f.write(password)
    print("Wrote password to file \"password.txt\"")

if __name__ == "__main__":
    main()
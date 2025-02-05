import string, random  # Importing necessary libraries

def random_password_generator():
    while True:
        try:
            # Taking user input for password length and ensuring it's at least 4
            length = int(input("Enter the length of your password (minimum 4): ").strip())
            if length >= 4:
                break
            else:
                print("Password should contain at least 4 characters.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Asking user for character preferences
    include_lowercase = input("Do you like to include Lower-Case characters? (y/n): ").strip().lower()
    include_uppercase = input("Do you like to include Upper-Case characters? (y/n): ").strip().lower()
    include_digits = input("Do you like to include digits? (y/n): ").strip().lower()
    include_specials = input("Do you like to include Special characters? (y/n): ").strip().lower()

    # Defining character pools based on user preferences
    lowercase = string.ascii_lowercase if include_lowercase == 'y' else ""
    uppercase = string.ascii_uppercase if include_uppercase == 'y' else ""
    digits = string.digits if include_digits == 'y' else ""
    specials = string.punctuation if include_specials == 'y' else ""

    all_characters = lowercase + uppercase + digits + specials  # Combining selected character sets

    required_characters = []  # Ensuring at least one of each selected character type is included
    if include_lowercase == 'y':
        required_characters.append(random.choice(lowercase))
    if include_uppercase == 'y':
        required_characters.append(random.choice(uppercase))
    if include_digits == 'y':
        required_characters.append(random.choice(digits))
    if include_specials == 'y':
        required_characters.append(random.choice(specials))

    remaining_length = length - len(required_characters)  # Calculating remaining password length
    password = required_characters  # Initializing password list

    # Filling the remaining length with random characters from the selected pools
    for _ in range(remaining_length):
        characters = random.choice(all_characters)
        password.append(characters)

    random.shuffle(password)  # Shuffling the password for randomness

    str_password = "".join(password)  # Converting list to string

    print("Generated Password: " + str_password)  # Displaying the generated password

random_password_generator()  # Calling the function to execute
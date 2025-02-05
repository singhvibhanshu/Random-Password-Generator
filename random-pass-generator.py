import string, random

def random_password_generator():
    length = int(input("Enter the length of your password: ").strip())
    include_lowercase = input("Do you like to include Lower-Case characters? (y/n): ").strip().lower()
    include_uppercase = input("Do you like to include Upper-Case characters? (y/n): ").strip().lower()
    include_digits = input("Do you like to include digits? (y/n): ").strip().lower()
    include_specials = input("Do you like to include Special characters? (y/n): ").strip().lower()

    if length < 8:
        print("Password should contains atleast 8 characters.")
        return
    
    lowercase = string.ascii_lowercase if include_lowercase == 'y' else ""
    uppercase = string.ascii_uppercase if include_uppercase == 'y' else ""
    digits = string.digits if include_digits == 'y' else ""
    specials = string.punctuation if include_specials == 'y' else ""

    all_characters = lowercase + uppercase + digits + specials

    required_characters = []
    if include_lowercase == 'y':
        required_characters.append(random.choice(lowercase))
    if include_uppercase == 'y':
        required_characters.append(random.choice(uppercase))
    if include_digits == 'y':
        required_characters.append(random.choice(digits))
    if include_specials == 'y':
        required_characters.append(random.choice(specials))

    remaining_length = length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length):
        characters = random.choice(all_characters)
        password.append(characters)

    random.shuffle(password)

    str_password = "".join(password)

    print(str_password)

random_password_generator()
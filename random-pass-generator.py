import string, random

def random_password_generator():
    length = int(input("Enter the length of your password: ").strip())
    include_uppercase = input("Do you like to include Upper-Case characters? (y/n): ").strip().lower()
    include_digits = input("Do you like to include digits? (y/n): ").strip().lower()
    include_specials = input("Do you like to include Special characters? (y/n): ").strip().lower()

    if length < 8:
        print("Password should contains atleast 8 characters.")
        return
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == 'y' else ""
    digits = string.digits if include_digits == 'y' else ""
    specials = string.punctuation if include_specials == 'y' else ""

    all_characters = lowercase + uppercase + digits + specials

    print(all_characters)

random_password_generator()
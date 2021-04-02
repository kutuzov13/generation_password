import random


# Templates for generator
DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '#$%&@'
CHARS = ''

ANSWER_OPTIONS = ('Да', 'ДА', 'да', 'Yes', 'YES', 'yes', 'y', 'Y')


def generate_password(length_password, chars_password) -> str:
    """Generation password."""
    password = ''
    for _ in range(length_password):
        password += random.choice(chars_password)
    return password


def save_password(name_password: str):
    """Saved password in new File."""
    with open('You Password.txt', 'a') as new_file:
        new_file.write(f'{name_password}: {generate_password(length, CHARS)}\n')
    return new_file


try:
    count = int(input('How many passwords to generate:\n'))
except ValueError:
    count = int(input('Please enter an integer!\n'))

try:
    length = int(input('Password length:\n'))
except ValueError:
    length = int(input('Please enter an integer!\n'))

in_numbers = input('Should numbers be included 0123456789?\n')
if in_numbers.lower() in ANSWER_OPTIONS:
    CHARS += DIGITS
else:
    CHARS += '0'

in_big_letters = input('Whether to include uppercase letters ?\n')
if in_big_letters.lower() in ANSWER_OPTIONS:
    CHARS += UPPERCASE_LETTERS
else:
    CHARS += '0'

in_small_letter = input('Should I include lowercase letters ?\n')
if in_small_letter.lower() in ANSWER_OPTIONS:
    CHARS += LOWERCASE_LETTERS
else:
    CHARS += '0'

symbols = input('Should symbols be included "#$%&@" ?\n')
if symbols.lower() in ANSWER_OPTIONS:
    CHARS += PUNCTUATION
else:
    CHARS += '0'

user_name_password = input('How to user_name_password your password?\n')

save = input('Want to save your password to a file?\n')
if save.lower() in ANSWER_OPTIONS:
    save_password(user_name_password)
else:
    print(f'Your password: {generate_password(length, CHARS)}')

# Generating the required number of passwords:
generate_password(length, CHARS)

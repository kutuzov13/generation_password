import random

# Templates for generator
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

answer_options = ('Да', 'ДА', 'да', 'Yes', 'YES', 'yes')


def generate_password(length_password, chars_password):
    """Generation password."""
    password = ''
    for _ in range(length_password):
        password += random.choice(chars_password)
    return password


def save_password(name_password):
    """Saved password in new File."""
    new_file = open('You_Password.txt', 'a')
    for _ in range(count):
        new_file.write(f'{name_password}: {generate_password(length, chars)}\n')
    new_file.close()
    return new_file


try:
    count = input('How many passwords to generate:\n')
    count = int(count)
except ValueError:
    count = input('Please enter an integer!\n')
    count = int(count)

try:
    length = input('Password length:\n')
    length = int(length)
except ValueError:
    length = input('Please enter an integer!\n')
    length = int(length)

in_numbers = input('Should numbers be included 0123456789?\n')
if in_numbers.lower() in answer_options:
    chars += digits
else:
    chars += '0'

in_big_letters = input('Whether to include uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ?\n')
if in_big_letters.lower() in answer_options:
    chars += uppercase_letters
else:
    chars += '0'

in_small_letter = input('Should I include lowercase letters abcdefghijklmnopqrstuvwxyz?\n')
if in_small_letter.lower() in answer_options:
    chars += lowercase_letters
else:
    chars += '0'

symbols = input('Should symbols be included "<!#$%&*+-=?№/@_>" ?\n')
if symbols.lower() in answer_options:
    chars += punctuation
else:
    chars += '0'

user_name_password = input('How to user_name_password your password?\n')

save = input('Want to save your password to a file?\n')
if save.lower() in answer_options:
    save_password(user_name_password)
else:
    print(f'Your password: {generate_password(length, chars)}')

# Generating the required number of passwords:
for passwords in range(count):
    generate_password(length, chars)

import random

# Шаблоны заведения пароля
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

# Функция генерации пароля
def generate_password(length, chars):
    password = '' #пустой пароль
    for _ in range(length): 
        password += random.choice(chars)
    return password

# Функция сохранения пароля в файл
def save_password():
    new_file = open('new_password.txt', 'a')
    for _ in range(1,count + 1):
        new_file.write(generate_password(length, chars) + '\n')
    new_file.close()
    return new_file

try:
    count = input('Какое колличество паролей сгенерировать:'+ '\n')
    count = int(count)
except ValueError:
    count = input('Введите целое число!(Если программа не получит целове число будет сгенерирован пустой пароль)' + '\n')
    count = int(count)

try:
    length = input('Длинна пароля:'+ '\n')
    length = int(length)
except ValueError:
    length = input('Введите целое число!(Если программа не получит целове число будет сгенерирован пустой пароль)' + '\n')
    length = int(length)

in_numbers = input('Включать ли цифры 0123456789?'+ '\n')
if in_numbers.lower() in ('Да', 'ДА', 'да', 'Yes', 'YES', 'yes'):
    chars += digits
else:
    chars += '0'

in_big_letters = input('Включить ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?'+ '\n')
if in_big_letters.lower() in ('Да', 'ДА', 'да', 'Yes', 'YES', 'yes'):
    chars += uppercase_letters
else:
    chars += '0'

in_small_lettrs = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?'+ '\n')
if in_small_lettrs.lower() in ('Да', 'ДА', 'да', 'Yes', 'YES', 'yes'):
    chars += lowercase_letters
else:
    chars += '0'

symbols = input('Включать ли символы "<!#$%&*+-=?№/@_>" ?'+ '\n')
if symbols.lower() in ('Да', 'ДА', 'да', 'Yes', 'YES', 'yes'):
    chars += punctuation
else:
    chars += '0'

save = input('Хотите сохранить пароль в файл?'+ '\n')
if save.lower() in ('Да', 'ДА', 'да', 'Yes', 'YES', 'yes'):
    print(save_password())
else:
    print('Как хотите но вот вам на всякий случай пароль!', generate_password(length, chars))

# Генерация нужного количества паролей:
for p in range(count):
    generate_password(length, chars)

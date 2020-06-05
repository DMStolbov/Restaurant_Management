def symbols_are_valid(text):
    if text == '':
        print('Your input is empty.')
        return False
    prohibited_symbols = [' ', '\t']
    for letter in text:
        if letter in prohibited_symbols:
            print('Do not use inappropriate symbols, please. (TAB, space)')
            return False
    return True


def is_unique(accounts, username):
    for account in accounts:
        if account['username'] == username:
            print(f'User {username} already exists.')
            return False
    return True


def only_letters(text):
    if text == '':
        print('Your input is empty.')
        return False
    allowed_symbols = list(' abcdefghijklmnopqrstuvwxyz') + list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    for letter in text:
        if letter.lower() not in allowed_symbols:
            return False
    return True

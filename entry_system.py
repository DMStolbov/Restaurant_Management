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


def starting_menu(accounts):
    print('Hello! Please, authorize.\n'
          '1. Sign up (new client)\n'
          '2. Sign in\n'
          '3. EXIT')
    while True:
        choice = input()
        if choice == '1':
            registration(accounts)
            break
        elif choice == '2':
            authorization(accounts)
            break
        elif choice == '3':
            quit()
        else:
            print('Inappropriate choice, please try again.')


def determine_relevant_menu(role):
    import specific_menus
    if role == 'manager':
        specific_menus.manager()
    elif role == 'cook':
        specific_menus.cook()
    elif role == 'waiter':
        specific_menus.waiter()
    elif role == 'client':
        specific_menus.client()


def info_from_database(file_name):
    users = open(file_name, 'r')
    data = users.read().split('\n')
    users.close()
    registered_users = []
    for i in range(len(data)):
        user_data = data[i].split('\t')
        user = {'username': user_data[0], 'password': user_data[1], 'role': user_data[2]}
        registered_users.append(user)
    return registered_users


def authorization(accounts):
    username = input('Username: ')
    password = input('Password: ')
    user_exists = False
    password_matches = False
    for account in accounts:
        if username == account['username'] and password == account['password']:
            print(f'Hello, {username.title()}! You logged in successfully. You are a {account["role"]}.')
            determine_relevant_menu(account["role"])
            password_matches = True
            user_exists = True
            break
        elif username == account['username'] and password != account['password']:
            user_exists = True
            break
    if not user_exists:
        print(f'User {username} not found.')
        print('Try again')
        authorization(accounts)
    elif not password_matches:
        print(f'{username.title()}, incorrect password.')
        print('Try again')
        authorization(accounts)


def registration(accounts):
    print('You may register now.')
    while True:
        username = input('Username: ')
        if symbols_are_valid(username) and is_unique(accounts, username):
            break
    while True:
        password = input('Password: ')
        if symbols_are_valid(password):
            break
    print("You have successfully registered")
    database = open('users.txt', 'a')
    database.write(f'\n{username}\t{password}\tclient')
    database.close()
    accounts = info_from_database('users.txt')
    starting_menu(accounts)

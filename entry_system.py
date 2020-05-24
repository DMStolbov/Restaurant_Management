def starting_menu(accounts):
    accounts = accounts
    print('Hello! Please, authorize.\n'
          'SIGN UP >>> input 1\n'
          'SIGN IN >>> input 2\n'
          'EXIT >>> input 3')
    while True:
        choice = input()
        if choice == '1':
            registration(accounts)
            break
        elif choice == '2':
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


def check_registered_users(file_name):
    users = open(file_name, 'r')
    data = users.read().split('\n')
    users.close()
    registered_users = []
    for i in range(len(data)):
        user_data = data[i].split('\t')
        user = {'username': user_data[0], 'password': user_data[1], 'role': user_data[2]}
        registered_users.append(user)
    return registered_users


username = ''
password = ''
role = ''


def authorization(accounts):
    global username
    global password
    accounts = accounts
    username = input('Username: ')
    password = input('Password: ')
    for account in accounts:
        if username == account['username']:
            if password == account['password']:
                print(f'Hello, {username.title()}! You logged in successfully. You are a {account["role"]}.')
                global role
                role = users_role(accounts, username)
                determine_relevant_menu(role)
                return True
            print(f'{username.title()}, incorrect password.')
            authorization(accounts)
    print(f'User {username} not found.')
    authorization(accounts)


def users_role(accounts, username):
    for account in accounts:
        if account['username'] == username:
            return account['role']


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


def registration(accounts):
    print('You may register now.')
    accounts = accounts
    while True:
        username = input('Username: ')
        if symbols_are_valid(username) and is_unique(accounts, username):
            break

    while True:
        password = input('Password: ')
        if symbols_are_valid(password):
            break

    available_roles = ['manager', 'cook', 'waiter', 'client']

    while True:
        role = input('Enter your role (manager, cook, waiter, client): ')
        if role in available_roles:
            break
        else:
            print('Incorrect role, please try again')

    # Appending the received data of a new user to the 'users.txt' file.
    database = open('users.txt', 'a')
    database.write(f'\n{username}\t{password}\t{role}')
    database.close()

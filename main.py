from entry_system import starting_menu, check_registered_users, authorization
# Getting information about existing users from a database.
accounts = check_registered_users('users.txt')

starting_menu(accounts)

# Updating information about existing users after a possible registration.
accounts = check_registered_users('users.txt')

# Authorization
print('You may log in now.')
authorization(accounts)
# Output - Menu for each user type (manager, cook, waiter and client).
# We can develop these in menu.py

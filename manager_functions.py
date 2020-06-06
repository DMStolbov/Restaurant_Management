from employees import *
from entry_system import *
from tools import only_letters


def employee_list():
    print('Staff list:')
    staff = employee_info('employees.txt')
    for emp in staff:
        print(emp.get_employee_info())


def hire_new_employee():
    while True:
        full_name = input('Full name: ')
        if only_letters(full_name):
            break
        else:
            print('Do not use inappropriate symbols in your fullname, please.')
    while True:
        position = input('Position: ')
        if position in ['manager', 'cook', 'waiter']:
            break
        else:
            print('Enter an appropriate position, please.')
    while True:
        salary = input('Salary: ')
        try:
            int(salary)
            break
        except ValueError:
            print('The salary should be an integer.')
    while True:
        experience = input('Experience in years: ')
        try:
            int(experience)
            break
        except ValueError:
            print('The experience should be an integer.')
    while True:
        username = input('Username: ')
        accounts = info_from_database('users.txt')
        if symbols_are_valid(username) and is_unique(accounts, username):
            break
    while True:
        password = input('Password: ')
        if symbols_are_valid(password):
            break
    print("You have successfully hired a new employee.")

    database = open('employees.txt', 'a')
    database.write(f'\n{full_name}```{position}```{salary}```{experience}')
    database.close()

    database = open('users.txt', 'a')
    database.write(f'\n{username}\t{password}\t{position}')
    database.close()


def check_reviews():
    print('Check reviews')

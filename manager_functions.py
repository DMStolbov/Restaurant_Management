from employees import *
from entry_system import *
from tools import only_letters
from exchange_rate import RUB_to_USD


def employee_list():
    exchange_rate = RUB_to_USD()
    print('Staff list:\n')
    staff = employee_info('employees.txt')
    i = 1
    for emp in staff:
        print(f'{i}.', emp.get_employee_info(exchange_rate))
        i += 1


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
        salary = input('Salary in USD: ')
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
    print('Reviews list:\n\n')
    reviews = open('reviews.txt', 'r')
    data = reviews.read().split('\n')
    reviews.close()
    reviews = []
    for review in data:
        attribute = review.split('--')
        reviews.append(attribute)
    i = 1
    for review in reviews:
        print(f'{i}. Waiter: {review[0]}\nEvaluation: {review[1]}\nClient comments: {review[2]}\n')
        i += 1

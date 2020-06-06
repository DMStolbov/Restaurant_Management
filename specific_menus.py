import manager_functions
import os


def manager():
    options = {
        '1': manager_functions.employee_list,
        '2': manager_functions.hire_new_employee,
        '3': manager_functions.check_reviews,
        '4': quit
    }
    print('Manager menu\n'
          '1. Proceed to the list of employees\n'
          '2. Hire a new employee\n'
          '3. Proceed to the list of reviews\n'
          '4. EXIT\n')
    while True:
        choice = input('')
        if choice in options:
            options.get(choice)()
            print('')
            manager()
        else:
            print('Inappropriate choice, please try again.')


def cook():
    print('Cook menu')
    os.system("python cooks.py")


def waiter():
    while True:
        print('Waiter menu')
        first = 0
        while first < 1:
            print("Choose the option: Tables(1), Menu (2), Exit(3)")
            ans = input()
            try:
                int(ans)
            except ValueError:
                print("You should write just one integer number. Please, try again")
                continue
            first += 1
        ans = int(ans)
        if ans == 1:
            os.system("python waiters2.py")
        elif ans == 2:
            os.system("python dishes.py")
        elif ans == 3:
            break
        else:
            print("Try again")


def client():
    while True:
        print('Client menu: Leave a comment(1), See the menu(2), Exit(3)')
        ans = int(input())
        if ans == 1:
            os.system("python comments.py")
        if ans == 2:
            os.system("python dishes.py")
        if ans == 3:
            break

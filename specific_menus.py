import manager_functions


def manager():
    options = {
        '1': manager_functions.warehouse_check,
        '2': manager_functions.order_foodstuffs,
        '3': manager_functions.box_office_check,
        '4': manager_functions.employee_list,
        '5': manager_functions.hire_new_employee,
        '6': manager_functions.check_reviews,
        '7': quit
    }
    print('Manager menu\n'
          '1. Check the warehouse\n'
          '2. Order foodstuffs\n'
          '3. Check the box office\n'
          '4. Proceed to the list of employees\n'
          '5. Hire a new employee >>>\n'
          '6. Proceed to the list of reviews\n'
          '7. EXIT\n')
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


def waiter():
    print('Waiter menu')


def client():
    print('Client menu')

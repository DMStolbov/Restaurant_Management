def employee_info(file_name):
    users = open(file_name, 'r')
    data = users.read().split('\n')
    users.close()
    employees = []
    for employee in data:
        attribute = employee.split('```')
        if attribute[1] == "waiter":
            employees.append(attribute)
    staff = []
    for employee in employees:
        employee = employee[0]
        staff.append(employee)
    return staff

def see_names(staff_name):
    print("These are our waiters:")
    for i in range(len(staff_name)):
        print(staff_name[i])


def waiter(staff_name):
    print("These are our waiters:")
    for i in range(len(staff_name)):
        print(staff_name[i])
    print("Whom do you want to evaluate? Enter the name")
    while True:
        ans = input()
        if ans in staff_name:
            break
        elif ans not in staff_name:
            print("There is no such waiter. Try again")
            continue
    return ans

def evaluate():
    print("Rate him: from 0 to 10 (0 - very bad, 10 - perfect)")
    while True:
        ans = input()
        if ans in ['1','2','3','4','5','6','7','8','9','10','0']:
            break
        if ans not in ['1','2','3','4','5','6','7','8','9','10','0']:
            print("Try again")
            continue
    return ans


def write_comment():
    print("Write a comment on him: ")
    ans = input()
    return ans

def write_file(waiter, rate, comment, file_name):
    with open(file_name, 'a', encoding="utf-8") as f:
        f.write(f'{waiter}--{rate}--{comment}\n')



staff = employee_info('employees.txt')
man = waiter(staff)
rate = evaluate()
comment = write_comment()
file = write_file(man, rate, comment, "reviews.txt")

class Employee:
    def __init__(self, full_name, position, salary, experience):
        self.fullname = full_name
        self.position = position
        self.salary = salary
        self.experience = experience

    def get_employee_info(self, exchange_rate):
        return f"Name: {self.fullname}\nPosition: {self.position}\nSalary in $: {self.salary}\n" \
               f"Salary in ₽: {float(self.salary) * exchange_rate}\nExperience in years: {self.experience}\n"


def employee_info(file_name):
    users = open(file_name, 'r')
    data = users.read().split('\n')
    users.close()
    employees = []
    for employee in data:
        attribute = employee.split('```')
        employees.append(attribute)
    staff = []
    for employee in employees:
        employee = Employee(employee[0], employee[1], employee[2], employee[3])
        staff.append(employee)
    return staff


staff = employee_info('employees.txt')

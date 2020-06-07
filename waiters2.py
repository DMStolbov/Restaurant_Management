import datetime
from draw_check import print_check

class Table:
    def __init__(self, number, number_peop,  open, close, num_dishes, discount, money):
        self.number = number
        self.number_people = number_peop
        self.open_hours = open
        self.close_hours = close
        self.num_dish = num_dishes
        self.discount = discount
        self.money = money

    def change_money(self, moneys):
        self.money = self.money + moneys
        #self.money = without_disc - (without_disc*(self.discount/100))

    def count_the_final_bill(self):
        self.money = self.money - (self.money*((self.discount)/100))
        

    def change_people(self, number_people):
        self.number_people = number_people

    def see_description(self):
        print(f"The table number {self.number},",
              f" The number of people : {self.number_people},",
              f" Open hours : {self.open_hours},",
              f" Closed hours : {self.close_hours},"
              f" Number of dishes : {self.num_dish};"
              f" The discount: {self.discount}% ;"
              f" Bill without discount: {self.money}")

    def change_open_hours(self):
        global t
        nu = 0
        while nu < 1:
            first = 0
            while first < 1:
                print("Enter the hours: ")
                hours = input()
                try:
                    int(hours)
                except ValueError:
                    print("You should write just one integer number. Please, try again")
                    continue
                first += 1
            hours = int(hours)
            second = 0
            while second < 1:
                print("Enter the minutes: ")
                minutes = input()
                try:
                    int(minutes)
                except ValueError:
                    print("You should write just one integer number. Please, try again")
                    continue
                second += 1
            minutes = int(minutes)
            try:
                t = datetime.time(hours, minutes)
            except ValueError:
                print("Your format is incorrect")
                continue
            nu += 1
        self.open_hours = t
        if self.open_hours.hour >= 12 and self.open_hours.hour <= 14:
            self.discount = 10

    def change_closing_hours(self):
        nu = 0
        while nu < 1:
            first = 0
            while first < 1:
                print("Enter the hours: ")
                hours = input()
                try:
                    int(hours)
                except ValueError:
                    print("You should write just one integer number. Please, try again")
                    continue
                first += 1
            hours = int(hours)
            second = 0
            while second < 1:
                print("Enter the minutes: ")
                minutes = input()
                try:
                    int(minutes)
                except ValueError:
                    print("You should write just one integer number. Please, try again")
                    continue
                second += 1
            minutes = int(minutes)
            try:
                tim = datetime.time(hours, minutes)
            except ValueError:
                print("Your format is incorrect")
                continue
            nu += 1
        self.close_hours = tim

    def clear_data(self):
        self.number_people = 0
        self.open_hours = 0
        self.close_hours = 0
        self.num_dish = 0
        self.discount = 0
        self.money = 0

    def add_num_food(self, num_dishes1):   ### Number of dishes
        self.num_dish = self.num_dish + num_dishes1

    def change_discount(self):
        print("Are there additional discounts?: Yes/ No")
        while True:
            user = input()
            if user != "No" and user != "Yes":
                print("Try again")
                continue
            if user == "Yes":
                while True:
                    disc = input("Birthday (1); Wedding (2)\n")
                    if disc in ["1","2"]:
                        break
                    else:
                        print("Try again")
                        continue
                disc = int(disc)
                if disc == 1:
                    if self.discount == 0:
                        self.discount = 5
                        break
                    else:
                        self.discount = int((self.discount + 5) / 1.2)
                        break
                if disc == 2:
                    if self.discount == 0:
                        self.discount = 10
                        break
                    else:
                        self.discount = int((self.discount + 10) / 1.2)
                        break
            if user == "No":
                break


class Food:
    def __init__(self, number_table):
        self.number_table = number_table
        self.food = []

    def add_dishes(self, num_dishes):
        print("What do you want to add?")
        num = 0
        while num < num_dishes:
            specific_dish = input()
            self.food.append(specific_dish)
            num += 1

    def see_dishes(self):
        if self.food != []:
            for dish in self.food:
                print(dish)
        elif self.food == []:
            print("There are no dishes")

    def clear_food(self):
        self.food.clear()


# Creating tables and food_tab
def create_list_Table(file):
    common = []
    with open(file, 'r', encoding="utf-8") as f:
        number = int(f.readline())
        i = 0
        tables = []
        food_tab = []
        while i < number:
            line = f.readline()
            data = line.split(',')
            if data[2] != '0':
                data2 = data[2].split(':')
                hours, minutes = int(data2[0]), int(data2[1])
                dt2 = datetime.time(hours, minutes)
            else:
                dt2 = '0'
            if data[3] != '0':
                data3 = data[3].split(':')
                hours, minutes = int(data3[0]), int(data3[1])
                dt3 = datetime.time(hours, minutes)
            else:
                dt3 = '0'
            table = Table(int(data[0]), int(data[1]), dt2, dt3, int(data[4]), int(data[5]), int(data[6]))
            tables.append(table)
            foods = Food(int(data[0]))
            if int(data[4]) > 0:
                j = 0
                while j < int(data[4]):
                    line_food = f.readline()
                    line_food = line_food.split('\n')
                    # print(line_food[0])
                    foods.food.append(line_food[0])
                    j += 1
            food_tab.append(foods)
            i += 1
    common.append(tables)
    common.append(food_tab)
    return common


class Dishes:
    def __init__(self, name, price):
        self.name = name
        self.price = price



with open("dishes.txt", 'r', encoding="utf-8") as f:
    number_dish = int(f.readline())
    i = 0
    num = 0
    dishes = []
    ingridients = []
    while i < number_dish:
        line = f.readline()
        data = line.split(',')
        dish = Dishes(data[0], int(data[1]))
        dishes.append(dish)
        if int(data[3]) > 0:
            j = 0
            while j < int(data[3]):
                f.readline()
                j += 1
        i += 1



def write_into_tables(file):
    with open(file, "w", encoding="utf-8") as fi:
        fi.write('10\n')
        for i in range(10):
            fi.write('{},{},{},{},{},{},{}\n'.format(str(tables[i].number), str(tables[i].number_people),
                str(tables[i].open_hours), str(tables[i].close_hours), str(tables[i].num_dish),
                                               str(tables[i].discount), str(tables[i].money)))
            if tables[i].num_dish > 0:
                for dishh in foods[i].food:
                    fi.write(f'{dishh}\n')
    return file


def changes_in_tables(file, numb):
    # print("numb: ", numb)
    # print(tables[numb-1].number)
    with open(file, "a", encoding="utf-8") as fili:
        fili.write('Table number: {}; number of people: {}; opened in {}; '
                   'closed in {}; bill: {}\n'.format(tables[numb-1].number,
                        str(tables[numb-1].number_people), tables[numb-1].open_hours,tables[numb-1].close_hours,
                                                     tables[numb-1].money))

    return file


def back_option():
    while True:
        que = input("Enter to back: B ")
        if que == "B":
            break


def for_money():
    with open("money.txt", 'r', encoding="utf-8") as f:
        money = float(f.readline())
    return money

def write_tab(money):
    with open("money.txt", 'w', encoding="utf-8") as f:
        f.write(str(money))



def all_money(moneys, money_table):
    money = moneys + money_table
    return money


tables_and_food = create_list_Table("tables.txt")
tables = tables_and_food[0]
foods = tables_and_food[1]


names_dish = []
for l in range(number_dish):
    names_dish.append(dishes[l].name)


while True:
    print("Enter the number of the table you want to choose.If you want to exit, enter: Exit ")
    x = input()
    list_n = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    if x in list_n:
        x = int(x)
        print("You've chosen the table number ", x)
        for i in range(10):
            if tables[i].number == x:
                while True:
                    print(f"What do you want to choose (Table № {tables[i].number})\n"
                          "See the basic information about table (1)\n"
                          "Change the number of people (2)\n"
                          "Change the open hours (3)\n"
                          "Change the closed hours (4)\n"
                          "Add dishes (5)\n"
                          "Look at dishes (6)\n"
                          "Additional discounts (7)\n"
                          "Clear everything (8)\n"
                          "Print the check (All info will be nullified) (9)\n"
                          "Back (10)")
                    while True:
                        ans =input()
                        if ans in list_n:
                            break
                        else:
                            print("There is no such option. Try again")
                            continue
                    ans = int(ans)
                    if ans == 1:
                        print("The basic description: ")
                        tables[i].see_description()
                        back1 = back_option()
                    elif ans == 2:
                        print("How many people?")
                        num_pep = int(input())
                        tables[i].change_people(num_pep)
                        #ch1 = changes_in_tables('changes.txt', tables[i].number)
                        print("The information has ben changed")
                        back2 = back_option()
                    elif ans == 3:
                        tables[i].change_open_hours()
                        #ch2 = changes_in_tables('changes.txt', tables[i].number)
                        print("The information has ben changed")
                        back3 = back_option()
                    elif ans == 4:
                        tables[i].change_closing_hours()
                        #ch3 = changes_in_tables('changes.txt', tables[i].number)
                        print("The information has ben changed")
                        #print(tables[i].close_hours.hour)
                        back4 = back_option()
                    elif ans == 5:
                        print("These are dishes: ")
                        for dish in names_dish:
                            print(dish)
                        # print("Enter number of food you want to add: ")
                        # num_food = int(input())
                        first = 0
                        while first < 1:
                            print("Enter number of food you want to add: ")
                            num_food = input()
                            try:
                                int(num_food)
                            except ValueError:
                                print("You should write just one integer number. Please, try again")
                                continue
                            first += 1
                        num_food = int(num_food)
                        num1 = 0
                        while num1 < num_food:
                            while True:
                                print("What do you want to add?")
                                chosen_dish = input()
                                if chosen_dish in names_dish:
                                    foods[i].food.append(chosen_dish)
                                    for c in range(len(names_dish)):
                                        if chosen_dish == dishes[c].name:
                                            tables[i].change_money(dishes[c].price)
                                    break
                                else:
                                    print("There is no such dish.Try again")
                                    continue
                            num1 += 1

                        tables[i].add_num_food(num_food)   #????

                        #foods[i].add_dishes(num_food)
                        print("The information has ben changed")
                        back6 = back_option()
                    elif ans == 6:
                        print("Now you will see the dishes: ")
                        foods[i].see_dishes()
                        back7 = back_option()
                    elif ans == 7:
                        tables[i].change_discount()
                    elif ans == 8:
                        tables[i].clear_data()
                        foods[i].clear_food()
                        #ch4 = changes_in_tables('changes.txt', tables[i].number)
                        print("The information has ben changed")
                        back5 = back_option()
                    elif ans == 9:
                        tables[i].count_the_final_bill()
                        ch1 = changes_in_tables('changes.txt', tables[i].number)
                        money_l = for_money()
                        mon = all_money(money_l, tables[i].money)
                        mone = write_tab(mon)
                        x = print_check(tables[i].number_people, tables[i].open_hours, tables[i].close_hours,
                                                tables[i].discount, foods[i].food, tables[i].money)
                        tables[i].clear_data()
                        foods[i].clear_food()
                        back6 = back_option()
                    elif ans == 10:
                        break
                    else:
                        print("Please, Try again")
                break
    elif x == "Exit":
        break
    else:
        print("Try again")

rewrite_file = write_into_tables("tables.txt")

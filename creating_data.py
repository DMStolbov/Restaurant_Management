import datetime
from foods import Food
from tablee import Table

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
            table = Table(int(data[0]), int(data[1]), dt2, dt3, int(data[4]), int(data[5]))
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


def write_into_tables(file):
    with open(file, "w", encoding="utf-8") as fi:
        fi.write('10\n')
        for i in range(10):
            fi.write('{},{},{},{},{},{}\n'.format(str(tables[i].number), str(tables[i].number_people),
                str(tables[i].open_hours), str(tables[i].close_hours), str(tables[i].num_dish),
                                               str(tables[i].discount)))
            if tables[i].num_dish > 0:
                for dishh in foods[i].food:
                    fi.write(f'{dishh}\n')
    return file


def changes_in_tables(file, numb):
    # print("numb: ", numb)
    # print(tables[numb-1].number)
    with open(file, "a", encoding="utf-8") as fili:
        fili.write('Table number: {}; number of people: {}; opened in {}; closed in {}\n'.format(tables[numb-1].number,
                        str(tables[numb-1].number_people), tables[numb-1].open_hours,tables[numb-1].close_hours))

    return file

def back_option():
    while True:
        que = input("Enter: Back ")
        if que == "Back":
            break
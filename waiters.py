import datetime
from foods import Food
from tablee import Table
from creating_data import create_list_Table
from creating_data import write_into_tables
from creating_data import changes_in_tables
from creating_data import back_option


            
tables_and_food = create_list_Table("tables.txt")
tables = tables_and_food[0]
foods = tables_and_food[1]


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
                          "Back (9)")
                    ans = int(input())
                    if ans == 1:
                        print("The basic description: ")
                        tables[i].see_description()
                        back1 = back_option()
                    elif ans == 2:
                        print("How many people?")
                        num_pep = int(input())
                        tables[i].change_people(num_pep)
                        ch1 = changes_in_tables('changes.txt', tables[i].number)
                        print("The information has ben changed")
                        back2 = back_option()
                    elif ans == 3:
                        tables[i].change_open_hours()
                        ch2 = changes_in_tables('changes.txt', tables[i].number)
                        print("The information has ben changed")
                        back3 = back_option()
                    elif ans == 4:
                        tables[i].change_closing_hours()
                        ch3 = changes_in_tables('changes.txt', tables[i].number)
                        print("The information has ben changed")
                        print(tables[i].close_hours.hour)
                        back4 = back_option()
                    elif ans == 5:
                        print("Enter number of food you want to add: ")
                        num_food = int(input())
                        tables[i].add_num_food(num_food)   #????
                        foods[i].add_dishes(num_food)
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
                        ch4 = changes_in_tables('changes.txt', tables[i].number)
                        print("The information has ben changed")
                        back5 = back_option()
                    elif ans == 9:
                        break
                    else:
                        print("Please, Try again")
                break
    elif x == "Exit":
        break
    else:
        print("Try again")

rewrite_file = write_into_tables("tables.txt")

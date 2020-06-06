import datetime

class Table:
    def __init__(self, number, number_peop,  open, close, num_dishes, discount):
        self.number = number
        self.number_people = number_peop
        self.open_hours = open
        self.close_hours = close
        self.num_dish = num_dishes
        self.discount = discount

    def change_people(self, number_people):
        self.number_people = number_people

    def see_description(self):
        print(f"The table number {self.number},",
              f" The number of people : {self.number_people},",
              f" Open hours : {self.open_hours},",
              f" Closed hours : {self.close_hours},"
              f" Number of dishes : {self.num_dish}"
              f" The discount: {self.discount} %")

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

    def add_num_food(self, num_dishes1):   ### Number of dishes
        self.num_dish = self.num_dish + num_dishes1

    def change_discount(self):
        print("If there are additional discounts?: Yes/ No")
        while True:
            user = input()
            if user != "No" and user != "Yes":
                print("Try again")
                continue
            if user == "Yes":
                disc = int(input("Birthday (1); Wedding (2)\n"))
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
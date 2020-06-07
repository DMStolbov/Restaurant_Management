class Dishes:
    def __init__(self, name, price,  calories, num_ingr):
        self.name = name
        self.price = price
        self.calories = calories
        self.num_ingr = num_ingr
        self.ingridients = []


with open("dishes.txt", 'r', encoding="utf-8") as f:
    number_dish = int(f.readline())
    i = 0
    num = 0
    dishes = []
    ingridients = []
    while i < number_dish:
        line = f.readline()
        data = line.split(',')
        dish = Dishes(data[0], int(data[1]), int(data[2]), int(data[3]))
        dishes.append(dish)
        if int(data[3]) > 0:
            j = 0
            new_set = []
            while j < int(data[3]):
                line_ing = f.readline()
                line_ing = line_ing.split('\n')
                list_ing = line_ing[0].split(',')
                dishes[i].ingridients.append(list_ing)
                j += 1
        i += 1


def show_menu(num_dishes):
    print("Here is the menu!")
    k = 0
    new_names = []
    while k < num_dishes:
        print(f'{k+1}. Dish: {dishes[k].name}, Calories: {dishes[k].calories}, Price: {dishes[k].price}')
        new_names.append(dishes[k].name)
        k += 1
    while True:
        print("Do you want to see ingridients of a particular dish? Yes/ No")
        xx = input()
        if xx == "No":
            break
        elif xx == "Yes":
            while True:
                print("Enter the name of a dish: / Exit")
                user = input()
                if user in new_names:
                    break
                else:
                    print("There is no such dish. Please, try again")
                    continue
            if user == "Exit":
                break
            m = 0
            while m < 10:
                if user == dishes[m].name:
                    print(dishes[m].name)
                    for num1 in range(dishes[m].num_ingr):
                        #print(dishes[m].ingridients[0])
                        print(f'Name: {dishes[m].ingridients[num1][0]}, Number:{dishes[m].ingridients[num1][1]}')
                m += 1
        elif xx != "Yes" or xx != "No":
            print("Try again")
            continue



menu = show_menu(number_dish)
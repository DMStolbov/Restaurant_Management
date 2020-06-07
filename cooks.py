def grocery(goods_dict):
    while True:
        print("Welcome to the storage! How can I help you? ")
        x = input("1.View goods \n2.Add goods \n3.Back \n")
        if x == ('3' or "Back"):
            break
        elif x == ("1" or 'View goods'):
            print(goods_dict)
        elif x == ("2" or 'Add goods'):
            add_goods(goods_dict)
        else:
            print("I don't understand what you're talking about, try again .")


class cooks:
    def __init__(self, name, evaluation, salaries, persona):
        self.name = name
        self.evaluation = evaluation
        self.salaries = salaries
        self.persona = persona


def show_cooks(special_list):
    while True:
        a = input('1.see the staffs \n2.change salaries \n3.'
                  'change the evaluation \n4.Exit \n')
        if a == ('4' or "Exit"):
            print("ASTALAVISTA BABY")
            break
        elif a == '1':
            b = input("who ? = ")
            if b == '1' or b == 'Daniil':
                print(special_list[0].persona)
                print(special_list[0].salaries)
            elif b == "2" or b == "Chan":
                print(special_list[1].persona)
                print(special_list[1].salaries)
            elif b == "3" or b == "Anastasia":
                print(special_list[2].persona)
                print(special_list[2].salaries)
        elif a == '2':
            b = input("who ? = ")
            c = input("How much does the cook deserve ? = ")
            if b == '1' or b == 'Daniil':
                special_list[0].salaries = c
                print(special_list[0].salaries)
                print("salaries is changed")
            elif b == "2" or b == "Chan":
                special_list[1].salaries = c
                print(special_list[1].salaries)
                print("salaries is changed")
            elif b == "3" or b == "Anastasia":
                special_list[2].salaries = c
                print(special_list[2].salaries)
                print("salaries is changed")
        elif a == "3":
            b = input("who ? = ")
            if b == ("3" or "Anastasia"):
                print(special_list[2].persona)
        else:
            print("I don't understand what you're talking about, try again .")


def see_persona(cooks):
    print(cooks.persona)


class recipes:
    def __init__(self, name, difficulties, ingredients, rating):
        self.name = name
        self.difficulties = difficulties
        self.ingredients = ingredients
        self.rating = rating

    def myfunc(self, goods):
        for item in self.ingredients:
            if goods[item] < self.ingredients[item]:
                return False
        return True


def show_recipe(recipe_books):
    while True:
        for i in range(len(recipe_books)):
            print("{}. {}".format(i + 1, recipe_books[i].name))
        print("5. done")
        a = input("Choose one recipe : ")
        if a == ("1" or "Fried eggs"):
            print("Dish : {} \nDifficulty : {} \nIngredients : {} \nRating : {}".format(recipe_books[0].name,
                                                                           recipe_books[0].difficulties,
                                                                           recipe_books[0].ingredients,
                                                                                   recipe_books[0].rating))
        elif a == ("2" or "Tomato fried eggs"):
            print("Dish : {} \nDifficulty : {} \nIngredients : {} \nRating : {}".format(recipe_books[1].name,
                                                                           recipe_books[1].difficulties,
                                                                           recipe_books[1].ingredients,
                                                                                   recipe_books[1].rating))
        elif a == ("3" or "Fried fish"):
            print("Dish : {} \nDifficulty : {} \nIngredients : {} \nRating : {} ".format(recipe_books[2].name,
                                                                           recipe_books[2].difficulties,
                                                                           recipe_books[2].ingredients,
                                                                                         recipe_books[2].rating))
        elif a == ("4" or "Fried eggs with pork"):
            print("Dish : {} \nDifficulty : {} \nIngredients : {} \nRating : {} ".format(recipe_books[3].name,
                                                                           recipe_books[3].difficulties,
                                                                           recipe_books[3].ingredients,
                                                                                         recipe_books[3].rating))
        elif a == ("5" or "done"):
            break


def cooking(recipe_books, goods):
    while True:
        available = []
        not_available = []
        print('\n')
        for i in range(len(recipe_books)):
            if recipe_books[i].myfunc(goods):
                print("{}. {} -- available".format(i + 1, recipe_books[i].name))
                available.append(str(i + 1))
            else:
                print("{}. {} -- not available".format(i + 1, recipe_books[i].name))
                not_available.append(str(i + 1))
        print(str(len(recipe_books) + 1) + ". done\n")
        a = input("Which one do you want to cook?\n")
        if a == str(len(recipe_books) + 1):
            break
        elif a in not_available:
            print('Not enough ingredients ! ')
        elif a not in available:
            print('Just input integer ')
        else:
            for item in recipe_books[int(a) - 1].ingredients:
                goods[item] -= recipe_books[int(a) - 1].ingredients[item]
            print("Finish!!!")
            print(goods)


def add_goods(goods_dict):
    while True:
        print("\nAdd your goods' name and quantity")
        data3 = input("Enter your goods' name : ")
        if data3.isdigit():
            print("Input string for name ! ")
            continue
        elif data3 == "done":
            break
        data2 = input("Enter your quantity : ")
        if not data2.isdigit():
            print("Input integer for quantity ! ")
            continue
        if data3 in goods_dict:
            goods_dict[data3] += int(data2)
        else:
            goods_dict[data3] = int(data2)


###一開始的主頁面

initial_grocery = {"eggs": 6, "spoon of oil": 10, "spoon of salt": 10,
                   "tomatoes": 5, "fish": 6, "pork": 10}
cooking_books = []
cooking_books.append(recipes("Fried eggs - today special", "Low", {"eggs": 5, "spoon of oil": 1, "spoon of salt": 6}, "6/10"))
cooking_books.append(
    recipes("Tomato fried eggs", "Medium", {"eggs": 7, "spoon of oil": 2, "spoon of salt": 3, "tomatoes": 5}, "7/10"))
cooking_books.append(recipes("Fried fish", "Medium", {"spoon of oil": 2, "spoon of salt": 3, "fish": 1}, "8/10"))
cooking_books.append(
    recipes("Fried eggs with pork", "High", {"eggs": 3, "spoon of oil": 4, "spoon of salt": 3, "pork": 3}, "9/10"))

special_list = []
special_list.append(cooks("Daniil", "Good", "500000", "Nice man"))
special_list.append(cooks("Chan", "Bad", "100000", "asian baby"))
special_list.append(cooks("Anastasia", "Well done", "800000", "Nice girl"))

while True:
    print("============My Super Storage============")
    a = input('1.My storage \n2.View recipes \n3.'
              'Make a dish \n4.view cooks \n5.Exit \n')
    if a == ('5' or "Exit"):
        print("ASTALAVISTA BABY")
        break
    elif a == '1':
        grocery(initial_grocery)
    elif a == '2':
        show_recipe(cooking_books)
    elif a == "3":
        cooking(cooking_books, initial_grocery)
    elif a == "4":
        show_cooks(special_list)
    else:
        print("I don't understand what you're talking about, try again .")

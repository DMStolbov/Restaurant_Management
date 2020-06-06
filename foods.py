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
        
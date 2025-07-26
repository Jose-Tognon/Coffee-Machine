class CofeeMaker():
    def __init__(self):
        self.resources = {
            'Water':300,
            'Milk':200,
            'Coffee':100
        }
    def report(self):
        print(f'Water: {self.resources['Water']}ml')
        print(f'Milk: {self.resources['Milk']}ml')
        print(f'Coffee: {self.resources['Coffee']}g')

    def is_resources_sufficient(self,drink):
        is_makeable = True
        for item in drink.ingredients:
            if self.resources[item] >= drink.ingredients[item]:
                pass
            else:
                print(f'Sorry. There is not enough {item}')
                is_makeable = False
        return is_makeable

    def make_coffee(self,drink):
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f'Here is your {drink.name}. Enjoy')




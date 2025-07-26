from operator import concat


class MenuItem():
    def __init__(self,name,water,milk,coffee,cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            'Water':water,
            'Milk':milk,
            'Coffee':coffee
        }

class Menu():
    def __init__(self):
        self.menu = [MenuItem('latte',200,150,24,2.5),
        MenuItem('espresso',50,0,18,1.5),
        MenuItem('cappuccino',250,100,24,3)
        ]
    def get_items(self):
        options = ''
        for item in self.menu:
            options = concat(options,f'{item.name}/')
        return options
    def find_drink(self,order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        return None

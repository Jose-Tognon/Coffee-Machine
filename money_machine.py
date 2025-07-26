class MoneyMachine():
    coins = {'penny':0.01,
             'Nickel':0.05,
             'Dime':0.10,
            'Quarter':0.25}

    def __init__(self):
        self.Money = 0
    def report(self):
        print(f'Money: ${self.Money}')

    def make_payment(self,drink):
        money = 0
        for coin in self.coins:
            n_coins = input(f'How Many {coin}:')
            money = float(money) + float(n_coins) * float(self.coins[coin])
        if money >= drink.cost:
            money -= drink.cost
            self.Money += drink.cost
            if money == 0:
                pass
            else:
                print(f'Here is your change ${money:.2f}')
            return True
        else:
            print(f'There is not enough money to purchase an {drink.name}')
            return False



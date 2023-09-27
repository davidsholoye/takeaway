#As a customer
#So that I can check if I want to order something
#I would like to see a list of dishes with prices.

class Menu:

    def __init__(self):
        self.menu = {
            "burrito": 2.00,
            "crisps": 0.50,
            "chai latte": 3.20,
            "chicken": 1.45,
            "soup": 2.65
        }

    def list_items(self):
        return self.menu
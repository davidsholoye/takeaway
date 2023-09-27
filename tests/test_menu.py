from unittest.mock import Mock
from lib.menu import Menu

def test_if_items_list():
    the_menu = Mock()
    the_menu.list_items.return_value = {
            "burrito": 2.00,
            "crisps": 0.50,
            "chai latte": 3.20,
            "chicken": 1.45,
            "soup": 2.65
        }
    
    assert the_menu.list_items() == {
            "burrito": 2.00,
            "crisps": 0.50,
            "chai latte": 3.20,
            "chicken": 1.45,
            "soup": 2.65
        }
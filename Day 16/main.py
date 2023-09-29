from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

serve = True
while serve:
    choice = input(f"What would you like? {m.get_items()}: ")
    if choice == 'off':
        serve = False
    elif choice == 'report':
        print(cm.report())
    else:
        drink = m.find_drink(choice)

        if cm.is_resource_sufficient(drink) and mm.make_payment(drink.cost):
            cm.make_coffee(drink)


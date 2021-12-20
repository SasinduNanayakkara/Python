# import classes
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# creating objects
menu = Menu()
money_machine = MoneyMachine()
coffee_make = CoffeeMaker()
is_on = True

# until is_on true loop through
while is_on:
    options = menu.get_items()  # get menu items
    choice = input(f"What would you like({options})")

    if choice == "off": # if user says turn off the machine
        is_on = False
    elif choice == "report":  # if user want to get a report
        coffee_make.report()  # call coffee maker report and display the available ingredients
        money_machine.report()  # call money machine report and display total income
    else:
        drink = menu.find_drink(choice)  #
        if coffee_make.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):  # call find_drink method and check
            # there are enough amount of ingredients and the user paid enough money
            coffee_make.make_coffee(drink)  # make the coffee


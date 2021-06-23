from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_opt = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino: ")
    # Turn off the coffee machine by entering "off" to the prompt
    if choice == "off":
        is_on = False
    # Print report
    elif choice == "report":
        money.report()
        coffee.report()
    elif choice == "options":
        menu_opt.get_items()
    else:
        # check if name provided is the name of a drink in the machine
        if menu_opt.find_drink(choice):
            drink = menu_opt.find_drink(choice)
            can_make = coffee.is_resource_sufficient(drink)
            if can_make:
                # check if there are enough resources to make the drink
                # cost = drink.cost
                if money.make_payment(drink.cost):
                    coffee.make_coffee(drink)

# # solution from the class instructor
# while is_on:
#     options = menu.get_items()
#     choice = input(f"What would you like? ({options}): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#         is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
#         is_payment_successful = money_machine.make_payment(drink.cost)
#         if is_enough_ingredients and is_payment_successful:
#             coffee_maker.make_coffee(drink)
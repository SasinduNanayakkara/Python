MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

income = 0

def report(income):
    for key in resources:
        print(f"{key} : {resources[key]}")
    
    print(f"income : {income}")

def checkCoins(drink):

    if drink == "espresso":
        total = 1.5
    elif drink == "latte":
        total = 2.5
    elif drink == "cappuccino":
        total = 3.0
    
    print("please insert coins")
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nikkels = int(input("How many nikkels? : "))
    pennies = int(input("How many pennies? : "))

    total_coins = quarters * 0.25 + dimes * 0.10 + nikkels * 0.05 + pennies * 0.01

    if total_coins >= total:
        print(f"Here is ${round(total_coins - total,2)} in change")
        return round(total_coins,2)
    else:
        return -1

def checkIngredients(drink):
    for key in MENU[drink]["ingredients"]:
        if resources[key] > MENU[drink]["ingredients"][key]:
            return True
        else:
            print(f"Sorry there is no enough water")
            return False

def makeCoffee(drink):
    for key in MENU[drink]["ingredients"]:
        resources[key] -= MENU[drink]["ingredients"][key]
    
    print(f"Here is your {drink} ☕. Enjoy!")


def main(income):

    off = False
    
    while not off:
        drink = input("What would you like (espresso/latte/cappuccino)")

        if drink == "off":
            off = True
        elif drink == "report":
            report(income)
        elif drink == "espresso" or drink == "latte" or drink == "cappuccino":
            is_ingredient_available =  checkIngredients(drink)

            if is_ingredient_available == True:
                total_coins = checkCoins(drink)
                if total_coins > 0:
                    
                    income += total_coins
                    makeCoffee(drink)
                    main(income)
                else:
                    print("Sorry that's not enough money. Money refunded.")
                    main(income)

            else:
                main(income)

        else:
            print("Sorry, we don't have that. Please try again")
            main(income)

main(income)
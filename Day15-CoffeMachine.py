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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    """used to print resource"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resource(coffee):
    """When the user chooses a drink, the program should check if there are enough resources to make that drink."""
    for item in MENU[coffee]['ingredients']:
        if resources[item] >= MENU[coffee]['ingredients'][item]:
            return True
        else:
            print(f"Sorry there is not enough {item}.")
            return False


def check_transaction(coffee):
    """Check that the user has inserted enough money to purchase the drink they selected."""
    global profit
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    receive = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    price = MENU[coffee]['cost']

    if receive > price:
        change = receive - price
        print(f"Here is ${change} dollars in change.")
        print(f"Here is your {coffee} ☕. Enjoy!")
        profit += price
        return True
    elif receive == price:
        print("Enough money.")
        print(f"Here is your {coffee} ☕. Enjoy!")
        profit += price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


should_continue = True
while should_continue:
    action = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if action == 'report':
        report()
    elif action in ['espresso','latte','cappuccino']:
        if check_resource(action):
            if check_transaction(action):
                resources['water'] -= MENU[action]['ingredients']['water']
                resources['coffee'] -= MENU[action]['ingredients']['coffee']
                if action != 'espresso':
                    resources['milk'] -= MENU[action]['ingredients']['milk']
    elif action == 'off':
        should_continue = False
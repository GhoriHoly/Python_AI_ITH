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

# TODO: 1. Print Report for the remaining resources
# TODO: 2. Is it sufficient to make the coffee.
# TODO: 3. process coin
# TODO: 4. Check transaction successful
# TODO: 5. Make Coffe


def print_report(report_resources, report_money):
    print(f"Water: {report_resources['water']}\nMilk: {report_resources['milk']}\n"
          f"Coffee: {report_resources['coffee']}\nMoney: ${report_money}")


def is_enough_resources(order_ingredients):
    """Checking is enough resources returns true otherwise returns false is not enough resources"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coin():
    """Returns the total calculates coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total

def is_transaction_sucessfull(money_received, drink_cost):
    """Returns true if the payment is successful or return false if the money is not sufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global current_money
        current_money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True
current_money = 0
current_resources = resources

while is_on:
    user_choice = input("What would you like? (espresso/latte/ cappuccino)")
    #print the MENU keys
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        print_report(current_resources, current_money)
    else:
        drink = MENU[user_choice]
        if is_enough_resources(drink['ingredients']):
            payment = process_coin()
            if is_transaction_sucessfull(payment, drink['cost']):
                make_coffee(user_choice, drink['ingredients'])











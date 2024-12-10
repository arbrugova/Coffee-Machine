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
money=0
# Functions
def remove_ingredients(drink):
    # Get the required ingredients for the drink
    water_cost = MENU[drink]["ingredients"]["water"]
    coffee_cost = MENU[drink]["ingredients"]["coffee"]

    # Deduct water and coffee (common to all drinks)
    resources["water"] -= water_cost
    resources["coffee"] -= coffee_cost

    # Check if milk is required and deduct it if it exists
    if "milk" in MENU[drink]["ingredients"]:
        milk_cost = MENU[drink]["ingredients"]["milk"]
        resources["milk"] -= milk_cost

def withdraw(balance):
    amount=float(input("Type amount you want to withdraw: $"))
    if amount>balance:
        print(f"Invalid amount you only have ${balance}")
    else:
        balance-=amount
        print(f"Withdraw successful.\nWithdraw amount: ${amount}\nBalance: ${balance}")
        return balance

def add_resources():
    resource = input("What do you want to add? :")
    amount = int(input("Type amount you want to add (50,100,200): "))

    if resource=="water" or resource=="coffee" or resource=="milk":
        resources[resource]+=amount
        print(f"Resource added, current {resource}: {resources[resource]}\n")
        print("Current resources:")
        show_report()
        print("\nType 'add' to add again")
    else:
        print("Resource not found")

def inputted_coins(quarters, dimes, nickles, pennies):
    total=0
    total+=(quarters*0.25)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01)
    return total

def transaction_check(drink, total):
    drink_cost=MENU[drink]["cost"]
    if total>drink_cost:
        remove_ingredients(drink)
        return True
    else:
        return False

def show_report():
    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffe: {resources["coffee"]}")
    print(f"Balance: ${money}")

def check_resources(drink_name):
    """
    Checks if there are enough resources to make the given drink.
    :param drink_name: The name of the drink (e.g., 'latte').
    :return: True if enough resources are available, otherwise False.
    """
    drink = MENU.get(drink_name)
    if not drink:
        print("Drink not found!")
        return False

    for ingredient, required_amount in drink['ingredients'].items():
        if resources.get(ingredient, 0) < required_amount:
            print(f"Sorry, not enough {ingredient}.")
            return False

    return True

machine_on_off=True
# Main function
while machine_on_off:
    user_input = input("What would you like? (espresso/latte/cappuccino):")

    if user_input=="espresso" or user_input=="cappuccino"or user_input=="latte":
        if check_resources(user_input):
            quarters = int(input("How many quarters: "))
            dimes = int(input("How many dimes: "))
            nickles = int(input("How many nickles: "))
            pennies = int(input("How many pennies: "))

            total=inputted_coins(quarters=quarters,dimes=dimes,nickles=nickles,pennies=pennies)
            drink_cost = MENU[user_input]["cost"]
            money += drink_cost
            change = total - drink_cost
            if transaction_check(drink=user_input, total=total):
                print(f"Here is your {user_input}")
                print(f"Here is {change:.2f} dollars in change.")
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif user_input=="report":
        show_report()
    elif user_input=="add":
        add_resources()
    elif user_input=="withdraw":
        money=withdraw(money)
    elif user_input=="off":
        machine_on_off=False

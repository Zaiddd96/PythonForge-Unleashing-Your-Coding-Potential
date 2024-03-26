import time

MENU = {
    "Star Drink": {
        "ingredients": {
            "water": 200,
            "sugar": 50,
            "white grape juice concentrate": 30,
            "green coffee extract": 20,
            "coconut cream": 100,
            "freeze-dried kiwi": 10,
        },
        "cost": 450,
    },
    "Coffee Frappuccino": {
        "ingredients": {
            "ice": 100,
            "milk": 200,
            "coffee frappuccino syrup": 50,
            "coffee": 24,
        },
        "cost": 390,
    },
    "Cappuccino": {
        "ingredients": {
            "espresso": 2,
            "steamed milk": 150,
            "milk foam": 150,
        },
        "cost": 350,
    },
    "Iced Caramel Macchiato": {
        "ingredients": {
            "ice": 100,
            "milk": 200,
            "vanilla syrup": 50,
            "espresso": 18,
            "caramel sauce": 20,
        },
        "cost": 400,
    },
    "Chai Tea Latte": {
        "ingredients": {
            "milk": 240,
            "chai tea concentrate": 120,
            "honey": 30,
            "cinnamon": 5,
        },
        "cost": 200,
    },
}

resources = {
    "water": 1000,
    "sugar": 500,
    "white grape juice concentrate": 300,
    "green coffee extract": 200,
    "coconut cream": 500,
    "freeze-dried kiwi": 100,
    "ice": 1000,
    "milk": 1000,
    "coffee frappuccino syrup": 500,
    "coffee": 500,
    "espresso": 500,
    "vanilla syrup": 500,
    "caramel sauce": 500,
    "chai tea concentrate": 500,
    "honey": 500,
    "cinnamon": 500,
}
total_earnings = 0


def display_menu():
    for drinks in MENU:
        print(f"{drinks} - ${MENU[drinks]['cost']}")


def generate_report():
    for key in resources:
        print(f"{key}: {resources[key]}g/ml")
    print(f"${total_earnings}")


def prepare_drink(coffee):
    global resources
    for ingredient, amount in MENU[coffee]["ingredients"].items():
        if ingredient not in resources or resources[ingredient] < amount:
            print(f"{ingredient} is not available.")
            return
    print("Please wait coffee is in process!")
    time.sleep(3)
    print(f"Here is your '{coffee}' Enjoy!!!")
    for ingredient, amount in MENU[coffee]["ingredients"].items():
        resources[ingredient] -= amount


def transaction(items):
    global total_earnings
    ten_dollar = int(input("How many $10: "))
    fifty_dollar = int(input("How many $50: "))
    hundred_dollar = int(input("How many $100: "))
    customer_payment = ten_dollar * 10 + fifty_dollar * 50 + hundred_dollar * 100
    item_costs = MENU[items]["cost"]
    if customer_payment > item_costs:
        change = customer_payment - item_costs
        print(f"Here is your change ${change}")
        total_earnings += item_costs
        return True
    elif customer_payment < item_costs:
        print(f"Sorry that's not enough money. Money refunded ${customer_payment}.")
        return False
    else:
        print(f"Transaction successful! wait for your {items}")
        total_earnings += item_costs
        return True


def starbucks():
    on = False
    print("⭐ 𝕊𝕋𝔸ℝ𝔹𝕌ℂ𝕂𝕊 ℂ𝕆𝔽𝔽𝔼𝔼 ⭐")
    while not on:
        print("Hey there, what's your pick today? 🎩")
        customer = input("Press 'M' to explore our magical menu ☕\n- Choose 'R' for a riveting report 📊\n- Or say "
                         "'off' to bid us adieu and close the machine! 🚪").lower()
        if customer == "off":
            on = True
        elif customer == "m":
            display_menu()
            while True:
                order = input("What would you like to order? ")
                if order in ["Star Drink", "Coffee Frappuccino", "Cappuccino", "Iced Caramel Macchiato",
                             "Chai Tea Latte"]:
                    break
                else:
                    print("Sorry your order is not available!")

            if transaction(order):
                prepare_drink(order)
                time.sleep(5)
            else:
                print("Please visit CCD!")
        elif customer == "r":
            generate_report()


starbucks()
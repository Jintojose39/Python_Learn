                    
logo=('''                       )     (
                 ___...(-------)-....___
             .-""       )    (          ""-.
       .-'``'|-._             )         _.-|
      /  .--.|   `""---...........---""`   |
     /  /    |                             |
     |  |    |                             |
      \  \   |                             |
       `\ `\ |                             |
         `\ `|                             |
         _/ /\                             /
        (__/  \                           /
     _..---""` \                         /`""---.._
  .-'           \                       /          '-.
 :               `-.__             __.-'              :
 :                  ) ""---...---"" (                 :
  '._               `"--...___...--"`              _.'
    \""--..__                              __..--""/
     '._     """----.....______.....----"""     _.'
        `""--..,,_____            _____,,..--""`
                      `"""----"""`
''')




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


def is_resource_sufficent(order_ingredients):
    '''Return True when order can be made , Return False when ingredients are insufficent'''
    # is_enough=True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:

            print(f"Sorry there is not enough {item}")
            # is_enough=False
            return False
    return True


def process_coins():
    '''Return the total calculated from the coins inserted'''
    total = int(input("How many quarters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.1
    total += int(input("How many nickels?:")) * 0.5
    total += int(input("How many pennies?:")) * 0.001
    return total


def is_transaction_successful(money_recived, drink_cost):
    '''Return True when the payment is accepted or False if the money is insufficent'''
    if money_recived >= drink_cost:
        change = round(money_recived - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        # profit in the global scope
        profit += drink_cost
        return True
    else:

        print("Sorry that's not enough money. Money refunded.")
        return False
def make_coffee(order_ingredients,drink_name):
    '''Deduct the required incredients from the resource incredients'''
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}.☕ Enjoy!!.")


is_on = True

while is_on:
    print(logo)
    choice = input("What would you like(espresso/latte/cappuccino)\n")
    if choice == "off":
        print("Thanks for using me have a nice day!!")
        is_on = False
    elif choice == "report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}gm")
        print(f"Money:${profit}")
    else:

        drink = MENU[choice]
        if is_resource_sufficent(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(drink["ingredients"],choice)



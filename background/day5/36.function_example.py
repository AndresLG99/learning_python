coffee_prices = [("capuccino",1.5),("espresso",1.2),("mocha",1.9)]

def priciest_coffee(lst_prices):

    highest_price = 0
    coffee_name = ""

    for c,p in lst_prices:
        if p > highest_price:
            highest_price = p
            coffee_name = c
        else:
            pass
    return (coffee_name, highest_price)

coffee, price = priciest_coffee(coffee_prices)

print(f"The priciest coffee is {coffee} at ${price}")
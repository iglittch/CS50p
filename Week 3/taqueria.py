def main():
    total = 0
    
    while True:
        try:
            order = input("Item: ")
            order = order.title()
            total = user_order(order,total)
            print(f"Total: ${total:.2f}")
        except KeyError:
            pass
        except EOFError:
            break


def user_order(item,total):
    menu_items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

    if item in menu_items:
        total += menu_items[item]
    return total

main()


# Prompt user to place order
# One per line adding each item's price to the total
# Display total cost prefixed with $ to 2 decimal places
# Case sensitive input
# Ignore any input that isnt in the list



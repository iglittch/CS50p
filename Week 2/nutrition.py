# Prompt user to input a fruit
# Output number of calories per portion
# Ignore input that isnt a fruit
def main():
    user_input = input("Fruit: ")
    user_input = user_input.lower()

    result = fda_check(user_input)

    print(f"Calories: {result}")

def fda_check(f):
    fruits = [
        {"name":"apple","calories":"130"},
        {"name":"avocado","calories":"50"},
        {"name":"banana","calories":"110"},
        {"name":"grapefruit","calories":"60"},
        {"name":"grapes","calories":"90"},
        {"name":"moneydew melon","calories":"50"},
        {"name":"kiwifruit","calories":"90"},
        {"name":"lemon","calories":"15"},
        {"name":"lime","calories":"20"},
        {"name":"nectrarine","calories":"60"},
        {"name":"orange","calories":"80"},
        {"name":"peach","calories":"60"},
        {"name":"pear","calories":"100"},
        {"name":"pineapple","calories":"50"},
        {"name":"plums","calories":"70"},
        {"name":"strawberries","calories":"50"},
        {"name":"sweet cherries","calories":"100"},
        {"name":"tangerine","calories":"50"},
        {"name":"watermelon","calories":"80"}
    ]

    for fruit in fruits:
        if fruit["name"] == f:
            return fruit["calories"]

main()
# Prompt user for greeting
def main():
    greeting = input("Bank Teller: ")
# Take care of case sensitivity, white space
    greeting = greeting.casefold().strip()

    compensation(greeting)


# If greeting == hello then 0
# if starts with h then 20
# otherwise 100
def compensation(welcome):
    if welcome.startswith("hello"):
        print("$0")
    elif welcome.startswith("h"):
        print("$20")
    else:
        print("$100")

main()


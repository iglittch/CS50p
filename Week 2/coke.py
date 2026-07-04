# Show coke bottle price
coke_price = 50
print(f"Amount Due: {coke_price}")

# Prompt user to insert a coin amount at a time
coin_paid = int(input("Insert Coin: "))
total_coins = coin_paid
amount_due = coke_price - coin_paid

if coin_paid in [25,10,5]:

    while amount_due != 0 and amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin_paid = int(input("Insert Coin: "))
        amount_due -= coin_paid
        total_coins += coin_paid

else:
    print("Invalid Coin")

change = total_coins - coke_price
if change > 0:
    print(f"Change Owed:{change}")

    
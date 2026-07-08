def main():
    grocery_list = []

    while True:
        try:
            grocery_item = input().upper()
            grocery_list.append(grocery_item)

        except EOFError:
            break
    
    grocery_list.sort()

    printed_list = set()

    for item in grocery_list:
        if item not in printed_list:
            item_count = grocery_list.count(item)
            print(f"{item_count} {item}") 
            printed_list.add(item)
    


main()
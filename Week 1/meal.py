# Prompt user for a time
# Output whether its breakfast, lunch or dinner time
# Default dont print anything
# Assume format will be 24-hour time ##:##
# Assume each meal time range is inclusive

def main():
    schedule = input("What time is it? ")
    schedule = convert(schedule)

    if 7.00 <= schedule <= 8.00:
        print("Breakfast time")
    elif 12.00 <= schedule <= 13.00:
        print("Lunch time")
    elif 18.00 <= schedule <= 19.00:
        print("Dinner time")
    else:
        print(" ")


def convert(time): 
    # 12 hour support
    if time.endswith("a.m."):
        time = time.replace(":",".").replace("a.m.","")
        time = float(time) 

        time = time - 12.00
        return time
    elif time.endswith("p.m."):
        time = time.replace(":",".").replace("p.m.","")
        time = float(time) 

        time = time + 12.00
        return time
    else:
        time = time.replace(":",".")
        time = float(time) 
        return time



if __name__ == "__main__":
    main()
# Prompt user for a time
# Output whether its breakfast, lunch or dinner time
# Default dont print anything
# Assume format will be 24-hour time ##:##
# Assume each meal time range is inclusive

def main():
    schedule = input("What time is it? ").strip()
    schedule = convert(schedule)

    if 7.00 <= schedule <= 8.00:
        print("breakfast time")
    elif 12.00 <= schedule <= 13.00:
        print("lunch time")
    elif 18.00 <= schedule <= 19.00:
        print("dinner time")
    else:
        print(" ")


def convert(time):
    # 12 hour support
    if time.endswith("a.m."):
        time = time.replace("a.m.","")
        hours,minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes) /60

        if hours == 12:
            hours = 0

        time = hours + minutes
        return time

    elif time.endswith("p.m."):
        time = time.replace("p.m.","")
        hours,minutes = time.split(":")

        hours = int(hours)
        minutes = int(minutes) /60

        if hours != 12:
            hours = hours + 12

        time = hours + minutes
        return time
    else:
        hours,minutes = time.split(":")

        minutes = int(minutes) /60
        hours = int(hours)

        time = hours + minutes
        return time



if __name__ == "__main__":
    main()

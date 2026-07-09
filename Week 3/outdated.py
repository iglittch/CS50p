def main():
    old_date = input("Date: ")
    new_date = modify_format(old_date)

    print(new_date)

def modify_format(date):
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    for m in months:
        if m in date:
            mm,dd,yyyy = date.split()

            dd = dd.replace(",","")
            mm = months.index(mm) + 1
            
            new_format = f"{yyyy}-{mm}-{dd}"

            return new_format

        else:
            mm,dd,yyyy = date.split("/")

            new_format = f"{yyyy}-{mm}-{dd}"

            return new_format
            


main()
def main():
    old_date = input("Date: ")
    new_date = modify_format(old_date)

    print(new_date)

class DayMonthYearInputError(Exception):
    pass

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
    while True:
        try:
            if "/" not in date:
                mm,dd,yyyy = date.split()

                dd = dd.replace(",","")
                mm = months.index(mm) + 1
                    
                dd = int(dd)
                if dd > 31 or dd < 1:
                    raise DayMonthYearInputError(dd)
                elif len(yyyy) > 4:
                    raise DayMonthYearInputError(yyyy)
                
                new_format = f"{yyyy}-{mm:02d}-{dd:02d}"

                return new_format

            else:
                mm,dd,yyyy = date.split("/")
                dd = int(dd)
                mm = int(mm)

                
                if mm > 12 or mm < 1:
                    raise DayMonthYearInputError(mm)
                elif dd > 31 or dd < 1:
                    raise DayMonthYearInputError(dd)
                elif len(yyyy) > 4:
                    raise DayMonthYearInputError(yyyy)
                else:
                    new_format = f"{yyyy}-{mm:02d}-{dd:02d}"

                return new_format
            
        except (DayMonthYearInputError,ValueError) as error:
            date = input("Date: ")
        


main()


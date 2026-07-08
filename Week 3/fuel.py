from fractions import Fraction

def main():
    tank_level = check_fraction("What is x/y? ")

    current_level = get_percentage(tank_level)

    print(current_level)

def check_fraction(prompt):
    
    while True:
        try:
            return Fraction(input(prompt))
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

    
def get_percentage(z):
    level = z * 100
    if level >= 99:
        return "F"
    if level <= 1:
        return "E"
    else:
        return f"{level}%"
    

main()
# Prompt user for fraction
# Format of prompt is x/y
# x is a non negative integer
# y is a positive integer

# output is a percentage rounded to the nearest int
# if output is 1% output E
# if output is 99% output F

# Exceptions (ValueError and ZeroDivisionError)
# - x or y is not an int
# - x is greater that y
# - y is zero

from fractions import Fraction

def main():
    tank_level = check_fraction("What is x/y? ")

    current_level = get_percentage(tank_level)

    print(current_level)

class ImproperFractionError(Exception):
    """Raised when the numerator is greater than the denomenator"""
    pass

class NegativeNumeratorError(Exception):
    """Raised if the numerator is negative"""
    pass

def check_fraction(prompt):
    
    while True:
        try:
            x = Fraction(input(prompt))

            if x.numerator > x.denominator :
                raise ImproperFractionError(x)
            elif x.numerator < 0:
                raise NegativeNumeratorError(x)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except ImproperFractionError as error:
            pass
        except NegativeNumeratorError as error:
            pass
        else:
            return x

    
def get_percentage(z):
    level = round(z * 100)
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

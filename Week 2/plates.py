import string

def main():
    # Prompt user for vanity plate
    # Check validity
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        if number_position(s) and char_check(s):
            return True
        else:
            return False
    else:
        return False

def number_position(y):
    # Once a number appears the rest must all be digits
    # First number apperaring must not be 0
    for i,char in enumerate(y):
        if char.isdigit():
            if not y[i:].isdigit():
                return False
            if char == "0":
                return False
            return True
    return False
            
            
    
def char_check(x):
    for char in x:
        if char not in string.punctuation and char not in string.whitespace:
            continue
        return False
    return True
        
            
main()
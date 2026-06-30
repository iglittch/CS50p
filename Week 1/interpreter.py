import operator
def main():
    # Prompt for the expressions
    expression = input("Calculate: ")
    # Split spaces btwn x y z assuming the spaces
    x,y,z = expression.split(" ")
    x = int(x)
    z = int(z)
    y = convert_operator(y)

    # Formulate calculations
    # Output numbers correct to 1 decimal place
    print(f"{y(x,z):.1f}")


def convert_operator(op):
    match op:
        case "+":
            return operator.add
        case "-":
            return operator.sub
        case "*":
            return operator.mul
        case "/":
            return operator.truediv
        case _:
            return operator.eq()

main()
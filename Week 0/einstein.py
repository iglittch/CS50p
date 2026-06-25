# Prompt user for mass
# Convert input to int
def main():
    mass = int(input("What is the mass?"))
    answer = equation(mass)

    print(f"Joules:{answer}")


# Calculate Joules
def equation(m):
    # Equation : e = mc2
    c = 300000000 
    e = m * pow(c,2)

    return e

main()



    


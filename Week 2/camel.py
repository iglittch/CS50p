# Prompt user for variable name in camelcase
def main():
    variable_name = input("camelCase: ")

    # Assume user input will be in camelcase
    modified_name = convert_to_snake(variable_name)
    # Output the input name to snake case
    print(f"Snake Case: {modified_name}")

def convert_to_snake(name):
    char_list = []

    for i,char in enumerate(name):
        if char.isupper() and i != 0:
            char_list.append("_")
        char_list.append(char)

    new_name = "".join(char_list).lower()
    return new_name

    

main()
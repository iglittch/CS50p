import inflect

p = inflect.engine()

name_list = []

while True:
    try:
        name = input("Name: ")
    
        name_list.append(name)
    
    except EOFError:
        break

joint_names = p.join(name_list)
print(f"Adieu,adieu, to {joint_names}")

# Prompt user for name one per line until ctrl d
# Assume user will input at least one name
# Output adieu to those names
# Separate two names with one and
# Three with two commas and one and
# Rest with n - 1 commas and one and
def main():
# Prompt user for answer
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
# Take care of case sensitivity
    answer = answer.casefold()
# If answer is 42 print yes
    if answer == "42" or answer == "forty two" or answer == "forty-two" or answer == "fortytwo":
        print("Yes")
    else:
        print("No")
# Otherwise no

main()
# Prompt user for str
def main():
    text = input("Input: ")

    new_text = shorten(text)

    # Output without vowels
    print(f"Output: {new_text}")


def shorten(old_text):
    char_list = []

    for char in old_text:
        if char in list('aeiouAEIOU'):
            char_list.append("")
        else:
            char_list.append(char)
    
    new_text = "".join(char_list)
    return new_text


main()
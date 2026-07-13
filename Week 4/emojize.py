import emoji

def main():
    alias = input("Code: ")

    converted_alias = convert_to_emoji(alias)

    print(f"Emoji Version: {converted_alias}")

def convert_to_emoji(code):
    result = emoji.emojize(code)
    return result

main()

"""
Prompt user for str
Output emojized version
Convert any codes into corresponding emoji
"""
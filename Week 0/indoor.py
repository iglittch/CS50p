def main():
    #Prompt the user input
    voice = input()
    voice = volumeDown(voice)
    print(voice)


def volumeDown(tone):
    #Output the same input in lowercase
    return tone.lower()

main()
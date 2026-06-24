#Create main function
def main():
    text = input()
    final_text = convert(text)
    print(final_text)



#Implement the function to convert emoticons to emojis and prints result
def convert(message):
    return message.replace(":)","🙂").replace(":(","🙁")

#Call main fuction
main()
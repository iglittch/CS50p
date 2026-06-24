#Prompt user for input
voice = input("What would you like to break down? ")

#Print with modified separator
voice = voice.split(" ")
voice = "...".join(voice)

print(voice)
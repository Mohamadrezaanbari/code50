#Receive input from the user
playback= input("what's your playback?")

#Place three dots insted of space
playback = playback.replace(" ", "...")

#remove white space from the str
playback = playback.strip()

#Print the out put
print(f"{playback}")


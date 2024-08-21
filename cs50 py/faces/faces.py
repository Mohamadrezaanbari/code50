#ask the user for what i can to do
faces = input("what i can to do?")

#remove white space from the str
faces = faces.strip()

#place emoji insted of emoticons
faces = faces.replace(":)", "🙂")
faces = faces.replace(":(", "🙁")

# capitalaize the first letter of each word
faces = faces.title()

print(f"{faces}")

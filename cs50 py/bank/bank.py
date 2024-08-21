#entering to bank and greeting
user_input = input(" > ")

if user_input[:5].lower() =='hello':
    print("$0")
elif user_input.strip().lower()[:5] == 'hello':
    print("$0")
elif user_input[:3].lower().strip() == 'hey' or user_input[:3].lower().strip() == "how":
    print("$20")
else:
    print("$100")

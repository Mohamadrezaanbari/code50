# Get input from the user
user_iput = input("enter 42: ")

# Check the differnt conditions
if user_iput.strip() == '42':
    print("yes")
elif user_iput.lower() == 'forty two':
    print("yes")
elif user_iput.lower() == 'forty-two':
    print("yes")
else:
    print("no")

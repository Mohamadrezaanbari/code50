#Getting input from the user
user_input = input(' ')
user_input = user_input.split(' ')

#apply conditions
if user_input[1] == '+':
    result = float(user_input[0]) + float(user_input[2])
    print(float(result))
elif user_input[1] == '-':
    result = float(user_input[0]) - float(user_input[2])
    print(float(result))
elif user_input[1] == '/':
    result = float(user_input[0]) / float(user_input[2])
    print(float(result))
else: #user_input[0] == '*'
     result = float(user_input[0]) * float(user_input[2])
     print(result)
     
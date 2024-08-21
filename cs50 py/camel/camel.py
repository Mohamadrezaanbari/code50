camel_case = input("camelcase: ")

snake_case = ""

for i in range(len(camel_case)):
    if camel_case[i].isupper():
        snake_case = snake_case + "_" + camel_case[i].lower()
    else:
        snake_case += camel_case[i]

print("snake case", snake_case)
